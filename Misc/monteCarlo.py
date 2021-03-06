#!/usr/bin/env python3.6
import time  # realtime
startTime = time.time()

# modular file for splitting x.csv into test-train set by a ratio
import pandas as pd
from sklearn.model_selection import train_test_split
import os
import sys

# creating prepend variable for logging
prePend = "[ " + os.path.basename(sys.argv[0]) + " ] "

# outputting debug info
cwd = os.getcwd()
print(prePend, "Current wd: ", cwd)
print(prePend, "Args: ", str(sys.argv))

# first arg
# setting data folder path with possible args(a if condition else b)
dataFolderPath = "../../../DataSets/ml-20m/"  # this is the default path
dataFolderPath = dataFolderPath if len(sys.argv) == 1 else sys.argv[1]
print(prePend, "Data path: ", dataFolderPath)

# second arg
# setting data file name
dataFileName = "pML.csv"  # default value
dataFileName = sys.argv[2] if len(sys.argv) >= 3 else dataFileName
print(prePend, "Data file name: ", dataFileName)

# third arg
# setting test/train split
testSize = 0.2  # default value
testSize = float(sys.argv[3]) if len(sys.argv) >= 4 else testSize
print(prePend, "Split test %: ", testSize)

# fourth arg
# setting data output test file name
testFileName = "test.csv"  # default value
testFileName = sys.argv[4] if len(sys.argv) >= 5 else testFileName
print(prePend, "Data file name: ", testFileName)

# fifth arg
# setting data output train file name
trainFileName = "train.csv"  # default value
trainFileName = sys.argv[5] if len(sys.argv) >= 6 else trainFileName
print(prePend, "Data file name: ", trainFileName)

# check if data exists
if (os.path.isfile(dataFolderPath + trainFileName) and
    os.path.isfile(dataFolderPath + testFileName)):  # and 1 == 0:
    print(prePend, testFileName, " & ", trainFileName, " found... Skipping.")
else:  # else generate test train set CSVs
    print(prePend,  testFileName, " & ", trainFileName, "not found... Generating.")
    wholeData = pd.read_csv(dataFolderPath + dataFileName)
    train, test = train_test_split(wholeData, test_size=testSize)
    train.to_csv( (dataFolderPath + trainFileName), encoding='utf-8', index=False)
    test.to_csv( (dataFolderPath + testFileName), encoding='utf-8', index=False)

print(prePend, "Fin.", (time.time() - startTime), " seconds.")