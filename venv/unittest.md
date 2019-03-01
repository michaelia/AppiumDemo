#####  unittest
unittest.TestCase类
这个类的实例表示一个测试用例，默认的methodName是runTest，即最简单的测试用例类的定义只包含runTest方法的定义。
如果同时定义了runTest方法和以test开头命名的方法，会忽略runTest方法。如果要指定执行某些方法，可以这样：

##### setUp()
在执行每个测试用例之前被执行，任何异常（除了unittest.SkipTest和AssertionError异常以外）都会当做是error而不是failure，且会终止当前测试用例的执行。