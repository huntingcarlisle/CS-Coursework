module Direction where

{-
PROBLEM:

Given the data definition below, design a function named left
that consumes a compass direction and produces the direction
that results from making a 90 degree left turn.
-}


-- DATA DEFINITIONS
data Direction  = N | S | E | W deriving (Show, Eq)
-- interp. a compass direction that a player can be facing

{-
fn_for_Direction d
    | ((==) N d) = (...)
    | ((==) S d) = (...)
    | ((==) E d) = (...)
    | ((==) W d) = (...)
-}


-- FUNCTIONS
left :: Direction -> Direction
-- takes as input a Direction, returns Direction shifted 90 degrees counterclockwise

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (left N) W
            print $check_expect' (left E) N
            print $check_expect' (left S) E
            print $check_expect' (left W) S

left d -- = N
    | ((==) N d) = W
    | ((==) S d) = E
    | ((==) E d) = N
    | ((==) W d) = S
