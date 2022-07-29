from OMSimulator import OMSimulator
oms = OMSimulator()
model, status = oms.importFile("ball3.ssp")


oms.setResultFile(model, "results.csv")
oms.instantiate(model)
oms.initialize(model)
oms.simulate(model)
oms.terminate(model)
oms.delete(model)
print("result generated")