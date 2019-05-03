module SeatNum where

{-

PROBLEM:

Imagine that you are designing a program to manage ticket sales for a
theatre. (Also imagine that the theatre is perfectly rectangular in shape!)

Design a data definition to represent a seat number in a row, where each
row has 32 seats. (Just the seat number, not the row number.)
-}

-- DATA DEFINITIONS
data SeatNum = SeatNum Int deriving (Show, Eq)
-- interp. the index number of a seat in a row, from [1,32]
s1 = SeatNum 1
s2 = SeatNum 12
s3 = SeatNum 32

{-
fn_for_SeatNum (SeatNum sn) =
  (... sn)
-}

