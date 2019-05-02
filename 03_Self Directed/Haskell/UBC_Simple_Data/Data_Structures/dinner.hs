module Dinner where

{-
PROBLEM A:

You are working on a system that will automate delivery for
YesItCanFly! airlines catering service.
There are three dinner options for each passenger, chicken, pasta
or no dinner at all.

Design a data definition to represent a dinner order. Call the type
DinnerOrder.
-}


-- DATA DEFINITIONS
data DinnerOrder  = Empty | Chicken | Pasta deriving (Show, Eq)
-- interp. a customer's dinner order choice, false if no dinner at all

{-
fn_for_DinnerOrder d
    | ((==) Empty d) = (...)
    | ((==) Chicken d) = (...)
    | ((==) Pasta d) = (...)
-}

{-
PROBLEM B:

Design the function dinner_order_to_msg that consumes a dinner order
and produces a message for the flight attendants saying what the
passenger ordered.

For example, calling dinner-order-to-msg for a chicken dinner would
produce "The passenger ordered chicken."
-}

-- FUNCTIONS
dinner_order_to_msg :: DinnerOrder -> String
-- return message for flight attendant announcing order

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (dinner_order_to_msg Empty) "The customer did not order dinner"
            print $check_expect' (dinner_order_to_msg Chicken) "The customer ordered Chicken"
            print $check_expect' (dinner_order_to_msg Pasta) "The customer ordered Pasta"

dinner_order_to_msg d -- = ""
    | ((==) Empty d) = "The customer did not order dinner"
    | otherwise = "The customer ordered " ++ show d
