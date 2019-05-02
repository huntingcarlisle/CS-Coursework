module BumpUp where

-- DATA DEFINITIONS
data LetterGrade =    A | B | C deriving (Show, Eq)
-- interp. the letter grade in a course

{-
fn_for_letter_grade lg
    | ((==) A lg) = (...)
    | ((==) B lg) = (...)
    | ((==) C lg) = (...)
-}


-- FUNCTIONS
bump_up :: LetterGrade -> LetterGrade
-- takes a letter grade as input, returns next highest letter grade as output. If A is input, returns A

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (bump_up A) A
            print $check_expect' (bump_up B) A
            print $check_expect' (bump_up C) B

bump_up lg -- = A
    | ((==) A lg) = A
    | ((==) B lg) = A
    | ((==) C lg) = B