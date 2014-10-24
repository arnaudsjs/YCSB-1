import subprocess


PATH_TO_PLOT_SCRIPT = '/root/YCSB/Thesis/plot/increasing_load_consistency.R'

def plotCdf(dataAboutConsistency, outputFile):
    dataToPlot = dataAboutConsistency.getListTimeToReachConsistency()
    writePlotDataToFile(dataToPlot, outputFile)
    exitCode = subprocess.call(['Rscript', PATH_TO_PLOT_SCRIPT, outputFile, outputFile + '_plot.png'])
    if exitCode != 0:
        raise Exception("Execution of plotscript: \"" + PATH_TO_PLOT_SCRIPT + "\" failed")

def writePlotDataToFile(dataToWrite, outputFile):
    f = open(outputFile, 'w')
    for item in dataToWrite:
        f.write(str(item) + "\n")
    f.close()