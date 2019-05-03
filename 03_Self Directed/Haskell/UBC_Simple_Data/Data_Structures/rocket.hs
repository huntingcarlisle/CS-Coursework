module Rocket where

{-
PROBLEM:

Consider the following data definition from the Rocket practice problem.

We have designed a function has-landed?, but there are errors in the function design.
Uncomment the program below, and make the minimal changes possible to a) make this
program work properly and b) make the function design consistent.
-}

-- DATA DEFINITIONS
data RocketDescent a = Landed a | DescendingRocket a deriving (Show)
-- interp. Landed if rocket's descent has ended, otherwise number of kilometers left to earth

rd1 = DescendingRocket 100
rd2 = DescendingRocket 40
rd3 = DescendingRocket 0.5
rd4 = Landed 0

instance (Eq a) => Eq (RocketDescent a) where
  DescendingRocket x == DescendingRocket y = x == y
  Landed x == Landed y = True
  _ == _ = False

{-
fn_for_RocketDescent (RocketDescent rd)
  | ((==) Landed rd) = (...)
  | otherwise        = (... rd)
-}


-- FUNCTIONS
has_landed :: (Eq a, Num a) => RocketDescent a -> Bool
-- returns True is rocket has landed, otehrwise returns False

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (has_landed rd1) False
            print $check_expect' (has_landed rd2) False
            print $check_expect' (has_landed rd3) False
            print $check_expect' (has_landed rd4) True

has_landed rd = ((==) (Landed 0) rd)
--has_landed (DescendingRocket rd) = False