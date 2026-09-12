from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. 큐비트 1개, 클래식 비트 1개
qc = QuantumCircuit(1)

# 2. H 게이트로 중첩 만들기: |0> -> (|0> + |1>)/sqrt(2)
qc.h(0)

# 3. 모든 큐비트 측정
qc = qc.measure_all(inplace=False)

print("회로:")
print(qc)

# 4. Sampler로 실행 (로컬 statevector 시뮬레이터)
sampler = StatevectorSampler()

# shots=1000 번 돌림 (코인 1000번 던지는 느낌)
job = sampler.run([qc], shots=1000)
result = job.result()

# 결과 카운트 꺼내기
counts = result[0].data.meas.get_counts()
print("측정 결과:", counts)

# 5. 히스토그램 플롯
plot_histogram(counts)
plt.show()