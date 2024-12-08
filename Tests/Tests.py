import BestiaryParseTests
import ChestDataParseTests
import HeaderParseTests
import InitializeOffsetsTests
import TownManagerParseTests

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

changePassed, changeRan = TownManagerParseTests.runTests()
numberOfTestsPassed += changePassed
numberOfTestsRan += changeRan

changePassed, changeRan = BestiaryParseTests.runTests()
numberOfTestsPassed += changePassed
numberOfTestsRan += changeRan

print(f"{numberOfTestsPassed} out of {numberOfTestsRan} passed.")
