module Demolish where

{-
PROBLEM A:

You are assigned to develop a system that will classify
buildings in downtown Vancouver based on how old they are.
According to city guidelines, there are three different classification levels:
new, old, and heritage.

Design a data definition to represent these classification levels.
Call it BuildingStatus.
-}


-- DATA DEFINITIONS
data BuildingStatus = New | Old | Heritage deriving (Show, Eq)
-- interp. classification of building per city guidelines

{-
fn_for_building_status bs
    | ((==) New bs) = (...)
    | ((==) Old bs) = (...)
    | ((==) Heritage bs) = (...)
-}





{-
PROBLEM B:

The city wants to demolish all buildings classified as "old".
You are hired to design a function called to_demolish
that determines whether a building should be torn down or not
-}

-- FUNCTIONS
to_demolish :: BuildingStatus -> Bool
-- return True is building is old, false otherwise

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (to_demolish Old) True
            print $check_expect' (to_demolish New) False
            print $check_expect' (to_demolish Heritage) False

to_demolish bs = ((==) Old bs)