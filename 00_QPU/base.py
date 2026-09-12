from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.visualization import plot_histogram

# ⚠ 여기 두 값은 네가 직접 넣어야 함. 이 파일은 절대 깃허브/친구한테 그대로 주지 마라.
API_KEY = "P02Z-dFbZIPqzuwKpdmvNbqor2Jtt44IMK-U96wOLFPs"
INSTANCE_CRN = "crn:v1:bluemix:public:quantum-computing:us-east:a/aa1d225111e942c1b7835898cdcb9ea6:ec09793f-467a-4640-bb56-44f65e6db61e::"

# 사용할 백엔드 고르기: 셋 중 아무거나
BACKEND_NAME = @@@ # ibm_fez, ibm_marrakesh 로 바꿔도 됨

service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token=API_KEY,
    instance=INSTANCE_CRN,
)

backend = service.backend(BACKEND_NAME)
print("사용 백엔드:", backend.name, "| qubits:", backend.num_qubits)

# ==== 회로 생성 ====
# 원하는 회로 생성

# ==== 회로를 백엔드에 맞게 변환 ====
qc_t = transpile(@@@, backend=backend)
print("Transpile된 회로:")
print(qc_t)

# ==== Sampler 실행 ====
sampler = Sampler(backend)
job = sampler.run([qc_t], shots=@@@)
print("job id:", job.job_id())

result = job.result()
counts = result[0].data.meas.get_counts()
print("측정 결과:", counts)