import InitializeOffsetsTests

numberOfTestsPassed = 0
numberOfTests = 0

if not InitializeOffsetsTests.initializeOffsetsWithFreshWorld():
    print("initializeOffsetsWithFreshWorld failed. \n")
else:
    numberOfTestsPassed += 1
numberOfTests += 1

if not InitializeOffsetsTests.initializeOffsetsWithRevisedWorld():
    print("initializeOffsetsWithRevisedWorld failed. \n")
else:
    numberOfTestsPassed += 1
numberOfTests += 1

print(str(numberOfTestsPassed) + " out of " + str(numberOfTests) + " tests passed.")
