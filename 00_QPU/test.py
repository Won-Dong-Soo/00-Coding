from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()  # 저장된 계정 로드

backends = service.backends()
for b in backends:
    print(b.name, "| qubits:", b.num_qubits)