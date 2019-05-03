module Employees where

{-
PROBLEM A:

You work in the Human Resources department at a ski lodge.
Because the lodge is busier at certain times of year,
the number of employees fluctuates.
There are always more than 10, but the maximum is 50.

Design a data definition to represent the number of ski lodge employees.
Call it Employees.
-}

-- DATA DEFINITIONS
data Employees = Employees Int deriving (Show, Eq)
-- interp. the number of employees at the ski lodge

e1 = Employees 11
e2 = Employees 50

{-
fn_for_employees (Employees e) =
  (... e)
-}


-- FUNCTIONS
{-
PROBLEM B:

Now design a function that will calculate the total payroll for the quarter.
Each employee is paid $1,500 per quarter. Call it calculate-payroll.
-}
calculate_payroll :: Employees -> Int

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (calculate_payroll e1) ((*) 11 1500)
            print $check_expect' (calculate_payroll e2) ((*) 50 1500)

calculate_payroll (Employees e)= (*1500) e