module LetterGrade where

{-
PROBLEM:

You're working with a revised version of the LetterGrade data definition that
you saw in lecture to design a function that produces true if a given LetterGrade
represents a passing grade in a course. You're working through HtDF and have
completed the signature, purpose, stub and examples, but you're getting an
error message.  Uncomment the code in the box below and revise it until
all the tests run (even though several tests still fail).
-}

-- DATA DEFINITIONS --
data LetterGrade = A | B | C | D | F deriving (Show, Eq)
-- interp. a grade in a course

{-
fn_for_LetterGrade lg
  | ((==) A lg) = (...)
  | ((==) B lg) = (...)
  | ((==) C lg) = (...)
  | ((==) D lg) = (...)
  | ((==) F lg) = (...)
-}


-- FUNCTIONS --
is_passing :: LetterGrade -> Bool
-- Returns False if F is input, True otherwise

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (is_passing A) True
            print $check_expect' (is_passing B) True
            print $check_expect' (is_passing C) True
            print $check_expect' (is_passing D) True
            print $check_expect' (is_passing F) False

is_passing = not . (==) F