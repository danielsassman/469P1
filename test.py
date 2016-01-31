# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# *NOTE* on windows, you may need to use the python command instead of python3.
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1, func2, and func3, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2 func3
# 


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
#    follow a convention: to test a function named foobar, the test must be
#    named "test_foobar_#", where # may be any digits at the end, such as
#    "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS. Do not include any
#   unofficial helper functions. If you want to make helper definitions
#   to use while testing, those can also be added there for clarity.
# 
# # TO IMPLEMENT (not yet a feature):
# to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
# 
# A work in progress by Mark Snyder, Oct. 2015.

import unittest
import shutil
import sys
import os
import time
import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = ["fast_fib","reversed","is_prime","nub","zip_with","collatz", "file_report","check_sudoku"]

# things inside of classes that we also want to use as test names (the classes' methods)
SUB_DEFNS = []

RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################


#BEGIN EXTRAS SECTION
TEMP_FILE = ".deletable_temp_file.txt"
def make_file(msg,filename=".deletable_temp_file.txt"):
	f = open(filename,'w')
	f.write(msg)
	f.close()

# END EXTRAS SECTION

############################################################################
############################################################################



# enter batch mode by giving a directory to work on.
BATCH_MODE = (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))



# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
	
	
	#---------------------------------------------------------------------
	
	def test_fast_fib_1(self):  self.assertEqual(fast_fib(0),0)
	def test_fast_fib_2(self):  self.assertEqual(fast_fib(1),1)
	def test_fast_fib_3(self):  self.assertEqual(fast_fib(2),1)
	def test_fast_fib_4(self):  self.assertEqual(fast_fib(3),2)
	def test_fast_fib_5(self):  self.assertEqual(fast_fib(4),3)
	def test_fast_fib_6(self):  self.assertEqual(fast_fib(5),5)
	def test_fast_fib_7(self):  self.assertEqual(fast_fib(6),8)
	def test_fast_fib_8(self):  self.assertEqual(fast_fib(7),13)
	def test_fast_fib_9(self):  self.assertEqual(fast_fib(61),2504730781961)
	def test_fast_fib_10(self): self.assertEqual(fast_fib(43),433494437)
	def test_fast_fib_11(self): self.assertEqual(fast_fib(601),178684461669052552311410692812805706249615844217278044703496837914086683543763273909969771627106004287604844670397177991379601)
	def test_fast_fib_12(self): self.assertEqual(fast_fib(55),139583862445)
	
	#---------------------------------------------------------------------
	
	def test_reversed_1(self):  self.assertEqual(reversed([]),[])
	def test_reversed_2(self):  self.assertEqual(reversed([5]),[5])
	def test_reversed_3(self):  self.assertEqual(reversed([2,4,6,8]),[8,6,4,2])
	def test_reversed_4(self):  self.assertEqual(reversed([True, 3, "hat"]),["hat",3,True])
	def test_reversed_5(self):  self.assertEqual(reversed([1,1,1,2,1,1]),[1,1,2,1,1,1])
	def test_reversed_6(self):  self.assertEqual(reversed([1,3,5,2,4,6]),[6,4,2,5,3,1])
	def test_reversed_7(self):  self.assertEqual(reversed([5,5,5,5,5]),[5,5,5,5,5])
	def test_reversed_8(self):  self.assertEqual(reversed([1.1,2.2,3.3]),[3.3,2.2,1.1])
	def test_reversed_9(self):
		xs = [1,2,3,4,5,6]
		vs = reversed(xs)
		# the original list shouldn't be modified.
		self.assertEqual([1,2,3,4,5,6],xs)
	def test_reversed_10(self):
		# give test 9 more weighting.
		self.test_reversed_9()
	def test_reversed_11(self):
		xs = [1,2,3,4,5,6]
		id1 = id(xs) # memory location of the original list
		vs = reversed(xs)
		id2 = id(vs) # memory location of the returned list
		# they shouldn't match.
		self.assertFalse(id1==id2)
	def test_reversed_12(self):
		# give test 11 more weighting.
		self.test_reversed_11()
	
	#---------------------------------------------------------------------
	
	def test_is_prime_1(self): self.assertFalse(is_prime(-5))
	def test_is_prime_2(self): self.assertFalse(is_prime(0))
	def test_is_prime_3(self): self.assertFalse(is_prime(1))
	def test_is_prime_4(self): self.assertTrue(is_prime(2))
	def test_is_prime_5(self): self.assertTrue(is_prime(3))
	def test_is_prime_6(self): self.assertFalse(is_prime(4))
	def test_is_prime_7(self): self.assertTrue(is_prime(5))
	def test_is_prime_8(self): self.assertTrue(is_prime(41))
	def test_is_prime_9(self): self.assertFalse(is_prime(117))
	def test_is_prime_10(self): self.assertTrue(is_prime(1117))
	def test_is_prime_11(self): self.assertTrue(is_prime(11117))
	def test_is_prime_12(self): self.assertTrue(is_prime(49999))
	def test_is_prime_13(self): self.assertFalse(is_prime(200000000))
	
	#---------------------------------------------------------------------
	
	def test_nub_1(self):  self.assertEquals(nub([]),[])
	def test_nub_2(self):  self.assertEquals(nub([5]),[5])
	def test_nub_3(self):  self.assertEquals(nub([13,13,13]),[13])
	def test_nub_4(self):  self.assertEquals(nub([1,2,3,1,2,3,1,2,3]),[1,2,3])
	def test_nub_5(self):  self.assertEquals(nub([1,1,3,2,2,5,5,5,5,4]),[1,3,2,5,4])
	def test_nub_6(self):  self.assertEquals(nub([1,4,2,5,3,1,2,3,4,5,6,1,3,2]),[1,4,2,5,3,6])
	def test_nub_7(self):  self.assertEquals(nub([1,2,3,4,5]),[1,2,3,4,5])
	def test_nub_8(self):  self.assertEquals(nub([-3,-1,1,3,2,4,-2,-4]),[-3,-1,1,3,2,4,-2,-4])
	def test_nub_9(self):  self.assertEquals(nub([1,1,5,1,10,1,1,15,1,1]),[1,5,10,15])
	def test_nub_10(self): self.assertEquals(nub([1,2,3,2]),[1,2,3])
	def test_nub_11(self): self.assertEquals(nub([1,2,3,3]),[1,2,3])
	def test_nub_12(self): self.assertEquals(nub([1,2,3,1]),[1,2,3])
	
	#---------------------------------------------------------------------
	
	def test_zip_with_1(self):
		def add(x,y): return x+y
		self.assertEquals(zip_with(add, [1,2,3,4], [10,10,10,10]),[11,12,13,14])
	def test_zip_with_2(self):
		def add(x,y): return x+y
		self.assertEquals(zip_with(add, [1,2,3,4], [5,6,7,8]),[6,8,10,12])
	def test_zip_with_3(self):
		def mul(x,y): return x*y
		# first list has fewer elements.
		self.assertEquals(zip_with(mul, [2,3,4],  [5,5,5,5,5]), [10,15,20])
	def test_zip_with_4(self):
		def mul(x,y): return x*y
		# second list has fewer elements.
		self.assertEquals(zip_with(mul, [2,3,4,5,6,7,8],  [5,5,5]), [10,15,20])
		def mul(x,y): return x*y
		# first list has zero elements.
		self.assertEquals(zip_with(mul, [],  [5,5,5,5,5]), [])
	def test_zip_with_5(self):
		def mul(x,y): return x*y
		# second list has zero elements.
		self.assertEquals(zip_with(mul, [2,3,4,5,6,7,8],  []), [])
	def test_zip_with_6(self):
		def mul(x,y): return x*y
		# both lists have zero elements.
		self.assertEquals(zip_with(mul, [2,3,4,5,6,7,8],  []), [])
	
	def test_zip_with_7(self):  self.test_zip_with_1()
	def test_zip_with_8(self):  self.test_zip_with_2()
	def test_zip_with_9(self):  self.test_zip_with_3()
	def test_zip_with_10(self): self.test_zip_with_4()
	def test_zip_with_11(self): self.test_zip_with_5()
	def test_zip_with_12(self): self.test_zip_with_6()
	
	#---------------------------------------------------------------------
	
	def test_collatz_1(self):  self.assertEqual(collatz(1),[1])
	def test_collatz_2(self):  self.assertEqual(collatz(3),[3, 10, 5, 16, 8, 4, 2, 1])
	def test_collatz_3(self):  self.assertEqual(collatz(4),[4, 2, 1])
	def test_collatz_4(self):  self.assertEqual(collatz(5),[5, 16, 8, 4, 2, 1])
	def test_collatz_5(self):  self.assertEqual(collatz(10),[10, 5, 16, 8, 4, 2, 1])
	def test_collatz_6(self):  self.assertEqual(collatz(11),[11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
	def test_collatz_7(self):  self.assertEqual(collatz(17),[17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
	def test_collatz_8(self):  self.assertEqual(collatz(42),[42, 21, 64, 32, 16, 8, 4, 2, 1])
	def test_collatz_9(self):  self.assertEqual(collatz(100),[100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
	def test_collatz_10(self): self.assertEqual(collatz(8192),[8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
	def test_collatz_11(self): self.assertEqual(collatz(2),[2,1])
	def test_collatz_12(self): self.assertEqual(collatz(6),[6,3,10,5,16,8,4,2,1])
	def test_collatz_13(self): self.assertEqual(collatz(99),[99, 298, 149, 448, 224, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
	
	#---------------------------------------------------------------------
	
	def test_file_report_1 (self): make_file("1\n1\n1\n"); self.assertEqual(file_report(TEMP_FILE),(1.0,1,[1]))
	def test_file_report_2 (self): make_file("1\n2\n3\n"); self.assertEqual(file_report(TEMP_FILE),(2.0,2,[1,2,3]))
	def test_file_report_3 (self): make_file("1\n2\n2\n3\n"); self.assertEqual(file_report(TEMP_FILE),(2.0,2,[2]))
	def test_file_report_4 (self): make_file("1\n2\n3\n4\n"); self.assertEqual(file_report(TEMP_FILE),(2.5,2.5,[1,2,3,4]))
	def test_file_report_5 (self): make_file("1\n3\n2\n3\n1\n"); self.assertEqual(file_report(TEMP_FILE),(2.0,2,[1,3]))
	def test_file_report_6 (self): make_file("5\n5\n5\n25\n"); self.assertEqual(file_report(TEMP_FILE),(10.0,5,[5]))
	def test_file_report_7 (self): make_file("13\n6\n13\n3\n7\n29\n12\n1\n2\n14\n"); self.assertEqual(file_report(TEMP_FILE),(10.0,9.5,[13]))
	def test_file_report_8 (self): self.test_file_report_1()
	def test_file_report_9 (self): self.test_file_report_2()
	def test_file_report_10(self): self.test_file_report_3()
	def test_file_report_11(self): self.test_file_report_4()
	def test_file_report_12(self): self.test_file_report_5()
	def test_file_report_13(self): self.test_file_report_6()
	def test_file_report_14(self): self.test_file_report_7()
	
	#---------------------------------------------------------------------
	
	def test_check_sudoku_1(self):
		# a pretty regular pattern of a correct sudoku.
		grid = [[1,2,3, 4,5,6, 7,8,9],
			    [4,5,6, 7,8,9, 1,2,3],
			    [7,8,9, 1,2,3, 4,5,6],
			    
			    [2,3,4, 5,6,7, 8,9,1],
			    [5,6,7, 8,9,1, 2,3,4],
			    [8,9,1, 2,3,4, 5,6,7],
			    
			    [3,4,5, 6,7,8, 9,1,2],
			    [6,7,8, 9,1,2, 3,4,5],
			    [9,1,2, 3,4,5, 6,7,8],
			   ]
		self.assertTrue(check_sudoku(grid))
	
	def test_check_sudoku_2(self):
		# keeps repeating the top three rows. only columns are faulty.
		grid = [[1,2,3, 4,5,6, 7,8,9],
			    [4,5,6, 7,8,9, 1,2,3],
			    [7,8,9, 1,2,3, 4,5,6],
			    
			    [1,2,3, 4,5,6, 7,8,9],
			    [4,5,6, 7,8,9, 1,2,3],
			    [7,8,9, 1,2,3, 4,5,6],
			    
			    [1,2,3, 4,5,6, 7,8,9],
			    [4,5,6, 7,8,9, 1,2,3],
			    [7,8,9, 1,2,3, 4,5,6],
			    ]
		self.assertFalse(check_sudoku(grid))
	
	def test_check_sudoku_3(self):
		# keeps repeating the left three 3x3 groups. only rows are faulty.
		grid = [[1,2,3, 1,2,3, 1,2,3],
			    [4,5,6, 4,5,6, 4,5,6],
			    [7,8,9, 7,8,9, 7,8,9],
			    
			    [2,3,4, 2,3,4, 2,3,4],
			    [5,6,7, 5,6,7, 5,6,7],
			    [8,9,1, 8,9,1, 8,9,1],
			    
			    [3,4,5, 3,4,5, 3,4,5],
			    [6,7,8, 6,7,8, 6,7,8],
			    [9,1,2, 9,1,2, 9,1,2],
			   ]
		self.assertFalse(check_sudoku(grid))

	def test_check_sudoku_4(self):
		# rows are shuffled to have only 3x3 groups wrong.
		grid = [[1,2,3, 4,5,6, 7,8,9],
			    [2,3,4, 5,6,7, 8,9,1],
			    [3,4,5, 6,7,8, 9,1,2],
			    [4,5,6, 7,8,9, 1,2,3],
			    [5,6,7, 8,9,1, 2,3,4],
			    [6,7,8, 9,1,2, 3,4,5],
			    [7,8,9, 1,2,3, 4,5,6],
			    [8,9,1, 2,3,4, 5,6,7],
			    [9,1,2, 3,4,5, 6,7,8],
			   ]
		self.assertFalse(check_sudoku(grid))
		
	def test_check_sudoku_5(self):
		# only the extra 5 in the dead center is a problem.
		grid = [[1,2,3, 4,5,6, 7,8,9],
			    [4,5,6, 7,8,9, 1,2,3],
			    [7,8,9, 1,2,3, 4,5,6],
			    
			    [2,3,4, 5,6,7, 8,9,1],
			    [5,6,7, 8,5,1, 2,3,4],
			    [8,9,1, 2,3,4, 5,6,7],
			    
			    [3,4,5, 6,7,8, 9,1,2],
			    [6,7,8, 9,1,2, 3,4,5],
			    [9,1,2, 3,4,5, 6,7,8],
			   ]
		self.assertFalse(check_sudoku(grid))
		
	def test_check_sudoku_6(self):
		# way wrong...
		grid = [[1,1,1, 1,1,1, 1,1,1],
			    [1,1,1, 1,1,1, 1,1,1],
			    [1,1,1, 1,1,1, 1,1,1],
			    
			    [1,1,1, 1,2,3, 1,1,1],
			    [1,1,1, 4,5,6, 1,1,1],
			    [1,1,1, 7,8,9, 1,1,1],
			    
			    [1,1,1, 1,1,1, 1,1,1],
			    [1,1,1, 1,1,1, 1,1,1],
			    [1,1,1, 1,1,1, 1,1,1],
			   ]
		self.assertFalse(check_sudoku(grid))

	def test_check_sudoku_7(self):
		# another correct grid.
		grid = [[2,7,8, 4,6,9, 1,5,3],
		        [6,9,3, 1,2,5, 4,7,8],
		        [4,5,1, 7,8,3, 2,6,9],
		        
		        [7,6,5, 8,9,4, 3,2,1],
		        [3,4,2, 6,1,7, 9,8,5],
		        [8,1,9, 3,5,2, 6,4,7],
		        
		        [9,8,4, 5,3,6, 7,1,2],
		        [5,2,6, 9,7,1, 8,3,4],
		        [1,3,7, 2,4,8, 5,9,6],
			   ]
		self.assertTrue(check_sudoku(grid))

	def test_check_sudoku_8(self):
		# another correct grid.
		grid =([[7,8,6, 4,9,3, 2,5,1],
		 	    [3,2,1, 8,7,5, 4,9,6],
		        [9,4,5, 6,2,1, 8,7,3],
		         
		        [1,5,7, 9,3,8, 6,2,4],
		        [2,9,8, 5,4,6, 3,1,7],
		        [4,6,3, 7,1,2, 9,8,5],
		         
	            [8,1,2, 3,6,7, 5,4,9],
		        [6,7,4, 2,5,9, 1,3,8],
		        [5,3,9, 1,8,4, 7,6,2],
			 ])
		self.assertTrue(check_sudoku(grid))
	def test_check_sudoku_9(self): self.test_check_sudoku_1()
	def test_check_sudoku_10(self): self.test_check_sudoku_2()
	def test_check_sudoku_11(self): self.test_check_sudoku_3()
	def test_check_sudoku_12(self): self.test_check_sudoku_4()

	#---------------------------------------------------------------------
	
	#---------------------------------------------------------------------
	
	#---------------------------------------------------------------------
	
	
# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		# find all methods that begin with "test".
		fs = []
		want_all = wants==None
		
		for func in AllTests.__dict__:
			# append regular tests
			# drop any digits from the end of str(func).
			dropnum = str(func)
			while dropnum[-1] in "1234567890":
				dropnum = dropnum[:-1]
			
			if func in ['__doc__', '__module__']:
				continue
			# check if we want this one.
			want_this_one = want_all
			if wants != None:
				for w in wants:
					is_ec = dropnum==("test_extra_credit_"+w+"_")
					if is_ec:
						want_this_one = False
						break
					is_test = dropnum==("test_"+w+"_")
					check = is_test and ((not is_ec) or (is_ec and (not BATCH_MODE)))
					want_this_one = want_this_one or check
			
			if want_this_one:
				fs.append(AllTests(str(func)))
		
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test".
			fs = []
			want_all = wants==None
			for func in AllTests.__dict__:
				want_this_one = want_all
				if wants != None:
					for w in wants:
						is_ec = (str(func).startswith("test_extra_credit_"+w))
						want_this_one = want_this_one or is_ec
				
				if BATCH_MODE and want_this_one:
					fs.append(AllTests(str(func)))
			
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
#		filenames.extend(os.path.join(dirpath, filez))
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 tester4L.py gmason76_2xx_L4.py\"")
	want_all = len(sys.argv) <=2
	wants = []
	
	# remove batch_mode signifiers from want-candidates.
	want_candidates = sys.argv[2:]
	for i in range(len(want_candidates)-1,-1,-1):
		if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
			del want_candidates[i]
	
	if not want_all:
		print("args: ",sys.argv)
		for w in want_candidates:
			if w in REQUIRED_DEFNS:
				wants.append(w)
			elif w in SUB_DEFNS:
				wants.append(w)
			else:
				raise Exception("asked to limit testing to unknown function '%s'."%w)
	else:
		wants = None # signifies that we want them all.
	
	if not BATCH_MODE:
		run_file(sys.argv[1],wants)
	else:
		filenames = files_list(sys.argv[1])
	
# 		print(filenames)
	
		results = []
		for filename in filenames:
			try:
				print("\n\n\nRUNNING: "+filename)
				(tag, passed,tried,ec) = run_file(filename,wants)
				results.append((tag,passed,tried,ec))
			except SyntaxError as e:
				results.append((filename+"_SYNTAX_ERROR",0,1))	
			except ValueError as e:
				return (filename+"_VALUE_ERROR",0,1)
			except TypeError as e:
				return (filename+"_TYPE_ERROR",0,1)
			except ImportError as e:
				results.append((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
			except Exception as e:
				return (filename+str(e.__reduce__()[0]),0,1)
			
		print("\n\n\nGRAND RESULTS:\n")
		for (tag, passed, tried, ec) in results:
			print(("%.0f%%  (%d/%d, %dEC) - " % (passed/tried*100 + ec, passed, tried, ec))+tag)

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=[]):
	
	# move the student's code to a valid file.
	shutil.copyfile(filename,"student.py")
	# wait half a second for file I/O to catch up...
		
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import imp
	count = 0
	while True:
		try:
			import student
			imp.reload(student)
			break
		except ImportError as e:
			print("import error getting student.. trying again. "+os.getcwd(), os.path.exists("student.py"))
			time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			results.append((filename+"_SYNTAX_ERROR",0,1))	
		except ValueError as e:
			return (filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			return (filename+"_TYPE_ERROR",0,1)
		except ImportError as e:
			results.append((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
		except Exception as e:
			return (filename+str(e.__reduce__()[0]),0,1)
		except Exception as e:
			print("didn't get to import student yet... " + e)
	# but we want to re-load this between student runs...
	# the imp module helps us force this reload.s
	
	import student
	imp.reload(student)
	
	# make a global for each expected definition.
	def decoy(name):
		return (lambda x: "<no '%s' definition found>" % name)
		
	for fn in REQUIRED_DEFNS:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			print("\nNO DEFINITION FOR '%s'." % fn)	
	
	# create an object that can run tests.
	runner1 = unittest.TextTestRunner()
	
	# define the suite of tests that should be run.
	suite1 = TheTestSuite(wants)
	
	# let the runner run the suite of tests.
	ans = runner1.run(suite1)
	num_errors   = len(ans.__dict__['errors'])
	num_failures = len(ans.__dict__['failures'])
	num_tests    = ans.__dict__['testsRun']
	num_passed   = num_tests - num_errors - num_failures
	# print(ans)
	
	
	if BATCH_MODE:
		# do the same for the extra credit.
		runnerEC = unittest.TextTestRunner()
		suiteEC = TheExtraCreditTestSuite(wants)
		ansEC = runnerEC.run(suiteEC)
		num_errorsEC   = len(ansEC.__dict__['errors'])
		num_failuresEC = len(ansEC.__dict__['failures'])
		num_testsEC    = ansEC.__dict__['testsRun']
		num_passedEC   = num_testsEC - num_errorsEC - num_failuresEC
		print(ansEC)
	else:
		num_passedEC = 0
	
	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	
	tag = ".".join(filename.split(".")[:-1])
	return (tag, num_passed, num_tests,num_passedEC)

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()
