# %%
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def oracle_constant_0() -> QuantumCircuit:
    oracle = QuantumCircuit(2)
    return oracle


def oracle_constant_1() -> QuantumCircuit:
    oracle = QuantumCircuit(2)
    oracle.x(1)
    return oracle


def oracle_identity() -> QuantumCircuit:
    oracle = QuantumCircuit(2)
    oracle.cx(0, 1)
    return oracle


def oracle_not() -> QuantumCircuit:
    oracle = QuantumCircuit(2)
    oracle.x(0)
    oracle.cx(0, 1)
    oracle.x(0)
    return oracle


def get_oracle(oracle_type: str) -> QuantumCircuit:
    if oracle_type == "constant_0":
        return oracle_constant_0()
    if oracle_type == "constant_1":
        return oracle_constant_1()
    if oracle_type == "identity":
        return oracle_identity()
    if oracle_type == "not":
        return oracle_not()

    raise ValueError("unknown oracle_type")


def deutsch(oracle_type: str) -> str:
    qc = QuantumCircuit(2, 1)

    # q1을 |1>로 준비
    qc.x(1)

    # q0, q1에 H
    qc.h(0)
    qc.h(1)

    # 오라클 1회 적용
    oracle = get_oracle(oracle_type)
    qc.compose(oracle, qubits=[0, 1], inplace=True)

    # q0에 다시 H
    qc.h(0)

    # q0만 측정
    qc.measure(0, 0)

    backend = AerSimulator()
    compiled = transpile(qc, backend)

    result = backend.run(
        compiled,
        shots=1,
        seed_simulator=42,
    ).result()

    counts = result.get_counts()
    bit = max(counts, key=counts.get)

    if bit == "0":
        return "constant"
    return "balanced"


print(deutsch("constant_0"))
print(deutsch("constant_1"))
print(deutsch("identity"))
print(deutsch("not"))
# %%
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


n = int(input())
mask = list(map(int, input()))
bias = int(input())

qc = QuantumCircuit(n+1, n)
qc.x(n)
for i in range(n+1):
    qc.h(i)

for i in range(len(mask)):
    if mask[i] == 1:
        qc.cx(i, n)
if bias == 1:
    qc.x(n)
        
for i in range(n):
    qc.h(i)
for i in range(n):
    qc.measure(i, i)

backend = AerSimulator()
compiled = transpile(qc, backend)

result = backend.run(
    compiled,
    shots=1,
    seed_simulator=42,
).result()

counts = result.get_counts()
print(counts)
# bit = max(counts, key=counts.get)
# if '1' not in bit:
#     print("constant")
# else:
#     print("balance")
# %%
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


n = int(input())
secret = input()

def make_oracle(secret: str) -> QuantumCircuit:
    n = len(secret)
    ancilla = n

    oracle = QuantumCircuit(n + 1)

    # 문자열 오른쪽 비트가 q0
    for qubit, bit in enumerate(reversed(secret)):
        if bit == "1":
            oracle.cx(qubit, ancilla)

    return oracle

qc = QuantumCircuit(n+1, n)

qc.x(n)
for i in range(n+1):
    qc.h(i)

oracle = make_oracle(secret)
qc.compose(oracle, qubits = list(range(n+1)), inplace = True)

for i in range(n):
    qc.h(i)
for i in range(n):
    qc.measure(i, i)

backend = AerSimulator()
compiled = transpile(qc, backend)

result = backend.run(
    compiled,
    shots=1000,
    seed_simulator=42,
).result()

counts = result.get_counts()
bit = max(counts, key=counts.get)
print(bit)

# %%
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from math import pi

n = int(input())
m = int(input())
marked_states = []
for i in range(m):
    marked_states.append(input())

def phaze_oracle(marked_state : str) -> QuantumCircuit:
    oracle = QuantumCircuit(n)
    for i, x in enumerate(reversed(marked_state)):
        if x == "0":
            oracle.x(i)
    
    oracle.h(n-1)
    oracle.mcx(list(range(n-1)), n-1)
    oracle.h(n-1)
    for i, x in enumerate(reversed(marked_state)):
        if x == "0":
            oracle.x(i)
            
    return oracle
    
    
def diffuser():
    oracle = QuantumCircuit(n)
    for i in range(n):
        oracle.h(i)
    for i in range(n):
        oracle.x(i)
    
    oracle.h(n-1)
    oracle.mcx(list(range(n-1)), n-1)
    oracle.h(n-1)
    
    for i in range(n):
        oracle.x(i)
    for i in range(n):
        oracle.h(i)
        
    return oracle
    
qc = QuantumCircuit(n, n)

for i in range(n):
    qc.h(i)
    
for _ in range(round(pi/4*(n/m)**(1/2))):
    for i in range(m):
        oracle = phaze_oracle(marked_states[i])
        qc.compose(oracle, qubits = list(range(n)), inplace = True)
    oracle2 = diffuser()
    qc.compose(oracle2, qubits = list(range(n)), inplace = True)
    
for i in range(n):
    qc.measure(i, i)

backend = AerSimulator()
compiled = transpile(qc, backend)

result = backend.run(
    compiled,
    shots=1000,
    seed_simulator=42,
).result()

counts = result.get_counts()
print(counts)

# %%
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from math import pi

n = int(input())
secret = input()

def make_simon_oracle(secret: str) -> QuantumCircuit:
    n = len(secret)

    if any(bit not in "01" for bit in secret):
        raise ValueError("secret must be binary")

    if set(secret) == {"0"}:
        raise ValueError("secret cannot be 0...0")

    oracle = QuantumCircuit(2*n)

    # 고전적으로 f(x)를 생성하기 위한 매핑
    # x와 x xor secret은 같은 출력으로 가야 함
    mapping = {}

    used = set()
    output = 0

    for x in range(2**n):
        if x in mapping:
            continue

        partner = x ^ int(secret, 2)

        # 같은 출력값 할당
        mapping[x] = output
        mapping[partner] = output

        used.add(output)
        output += 1


    # truth table 기반 oracle 생성
    # |x>|0> -> |x>|f(x)>
    for x, y in mapping.items():
        x_bits = format(x, f"0{n}b")
        y_bits = format(y, f"0{n}b")

        # x 상태에서만 동작하도록 X + MCX 사용
        controls = []

        for i, bit in enumerate(reversed(x_bits)):
            if bit == "0":
                oracle.x(i)

        # 출력 비트 생성
        for i, bit in enumerate(reversed(y_bits)):
            if bit == "1":
                oracle.mcx(
                    list(range(n)),
                    n+i
                )

        # 복구
        for i, bit in enumerate(reversed(x_bits)):
            if bit == "0":
                oracle.x(i)

    return oracle

qc = QuantumCircuit(2*n, n)

for i in range(n):
    qc.h(i)

U_f = make_simon_oracle(secret)

qc.compose(U_f, qubits = list(range(2*n)), inplace = True)

for i in range(n):
    qc.h(i)
    qc.measure(i, i)


backend = AerSimulator()
compiled = transpile(qc, backend)

result = backend.run(
    compiled,
    shots=1000,
    seed_simulator=43,
).result()

counts = result.get_counts()
bits = list(counts.keys())

print(bits)

def solve_simon_secret(samples: list[str]) -> str:
    if not samples:
        raise ValueError("측정 결과가 없음")

    samples = [sample.replace(" ", "") for sample in samples]
    n = len(samples[0])

    if any(len(sample) != n for sample in samples):
        raise ValueError("모든 측정값의 길이가 같아야 함")

    # 같은 방정식과 000...0 제거
    rows = list({
        int(sample, 2)
        for sample in samples
        if int(sample, 2) != 0
    })

    pivot_bits = []
    rank = 0

    # 왼쪽 비트부터 피벗 선택
    for bit in range(n - 1, -1, -1):
        pivot = None

        for row in range(rank, len(rows)):
            if rows[row] & (1 << bit):
                pivot = row
                break

        # 이 열에 피벗이 없으면 자유변수
        if pivot is None:
            continue

        rows[rank], rows[pivot] = rows[pivot], rows[rank]

        # 다른 모든 행에서 현재 피벗 비트 제거
        for row in range(len(rows)):
            if row != rank and rows[row] & (1 << bit):
                rows[row] ^= rows[rank]

        pivot_bits.append(bit)
        rank += 1

        if rank == len(rows):
            break

    # Simon에서 secret을 하나로 정하려면 rank = n - 1이어야 함
    if rank < n - 1:
        raise ValueError(
            f"독립 방정식이 부족함: rank={rank}, 필요한 rank={n - 1}"
        )

    if rank == n:
        raise ValueError("0이 아닌 secret이 존재하지 않음")

    pivot_set = set(pivot_bits)

    free_bits = [
        bit
        for bit in range(n)
        if bit not in pivot_set
    ]

    if len(free_bits) != 1:
        raise ValueError(
            f"자유변수가 {len(free_bits)}개임. 측정값을 더 모아야 함"
        )

    # 0이 아닌 해를 얻기 위해 유일한 자유변수를 1로 설정
    secret = 1 << free_bits[0]

    # RREF 상태이므로 각 피벗 변수 계산
    for row_index, pivot_bit in enumerate(pivot_bits):
        row = rows[row_index]

        # 현재 알려진 변수들의 내적이 1이면
        # 피벗 변수도 1이어야 전체 XOR가 0
        if (row & secret).bit_count() % 2 == 1:
            secret |= 1 << pivot_bit

    result = format(secret, f"0{n}b")

    # 검증
    if result == "0" * n:
        raise ValueError("secret이 0으로 계산됨")

    for sample in samples:
        y = int(sample, 2)

        if (y & secret).bit_count() % 2 != 0:
            raise ValueError(
                f"{sample} · {result} != 0"
            )

    return result

print(solve_simon_secret(bits))

# %%
