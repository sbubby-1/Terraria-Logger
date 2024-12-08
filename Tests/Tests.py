import ChestDataParseTests
import HeaderParseTests
import InitializeOffsetsTests

numberOfTestsPassed = 0
numberOfTestsRan = 0

changePassed, changeRan = InitializeOffsetsTests.runTests()
numberOfTestsPassed += changePassed
numberOfTestsRan += changeRan

changePassed, changeRan = HeaderParseTests.runTests()
numberOfTestsPassed += changePassed
numberOfTestsRan += changeRan

changePassed, changeRan = ChestDataParseTests.runTests()
numberOfTestsPassed += changePassed
numberOfTestsRan += changeRan

print(f"{numberOfTestsPassed} out of {numberOfTestsRan} passed.")
