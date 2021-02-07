from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import os
import wfdb

#Opening the output file
fin = open("databaseHealth.csv",'w')
fin.write('RecordNumber,AveragePSD,Energy,NormalorNot\n')

for filename in os.listdir("allRecordsHealthy/attributeFiles"):
    
    #Obtain Records and Attributes
    recordNumber = filename.split(".atr")[0]
    record = wfdb.rdrecord('allRecordsHealthy/headDataFiles/%s' % recordNumber) 
    annot = wfdb.rdann('allRecordsHealthy/attributeFiles/%s' % recordNumber,'atr')
    
    #Labeling Data
    state = 1
    '''
    if max(annot.__dict__["symbol"],key=annot.__dict__["symbol"].count) == "N":
        state=1
    else:
        state=0
    '''
    
    #Plotting Record
    '''
    wfdb.plot_wfdb(record=record, title='Record %s' %recordNumber) 
    '''
    
    #flattening data
    ecgSig = record.__dict__['p_signal']
    ecgSig = [x[1] for x in ecgSig]
    
    #Preprocess signal to obtain PSD and Energy
    f, modEcgSig = signal.periodogram(ecgSig, 650000)
    freqs, psd = signal.welch(modEcgSig)
    
    #Plot the signal's PSD
    '''
    plt.figure(figsize=(5, 4))
    plt.semilogx(freqs, psd)
    plt.title('PSD: power spectral density')
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.tight_layout()
    plt.show()
    '''
    
    #Obtain average psd and Energy
    avgPSD = sum(psd)/len(psd)
    energy = sum(map(lambda x:x*x,ecgSig))
    
    #Write data into database
    fin.write('{},{:.10e},{},{}\n'.format(recordNumber,avgPSD,energy,state))
    
fin.close()