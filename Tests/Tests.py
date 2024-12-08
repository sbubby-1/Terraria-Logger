import HeaderParseTests
import InitializeOffsetsTests

numberOfTestsPassed = 0
numberOfTestsRan = 0

initializeOffsetsTestsPassed, initializeOffsetsTestsRan = (
    InitializeOffsetsTests.runInitializeOffsetTests()
)
numberOfTestsPassed += initializeOffsetsTestsPassed
numberOfTestsRan += initializeOffsetsTestsRan

headerParseTestsPassed, headerParseTestsRan = HeaderParseTests.runHeaderParseTests()
numberOfTestsPassed += headerParseTestsPassed
numberOfTestsRan += headerParseTestsRan

print(f"{numberOfTestsPassed} out of {numberOfTestsRan} passed.")
