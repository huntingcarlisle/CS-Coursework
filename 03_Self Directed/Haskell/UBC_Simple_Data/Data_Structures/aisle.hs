module Aisle where

data SeatNum = SeatNum Int deriving (Show)
-- Interp. Seat numbers in a row, 1 and 32 are aisle seats

--Examples
sn1 = SeatNum 1
sn2 = SeatNum 12
sn3 = SeatNum 32

{-
fn_for_seat_num (SeatNum sn) =
      (... sn)
-}

validSeat :: Int -> SeatNum
validSeat n
        | n < 1 || n > 32 = error "Invalid seat number"
        | otherwise       = SeatNum n


-- Functions
is_aisle :: SeatNum -> Bool

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (is_aisle sn1) True
            print $check_expect' (is_aisle sn2) False
            print $check_expect' (is_aisle sn3) True
            print $check_expect' (is_aisle (SeatNum 13)) False

is_aisle (SeatNum sn) =
      ((||)
        ((==) sn 1)
        ((==) sn 32))

