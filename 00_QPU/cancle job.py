from qiskit_ibm_runtime import QiskitRuntimeService

ID = "d4mcr143tdfc73dqavsg"
API_KEY = "P02Z-dFbZIPqzuwKpdmvNbqor2Jtt44IMK-U96wOLFPs"
INSTANCE_CRN = "crn:v1:bluemix:public:quantum-computing:us-east:a/aa1d225111e942c1b7835898cdcb9ea6:ec09793f-467a-4640-bb56-44f65e6db61e::"

service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token=API_KEY,
    instance=INSTANCE_CRN,
)

job = service.job(ID)
job.cancel()
print("취소 완료")