module BikeRoute where

-- DATA DEFINITIONS
data BikeRoute =    Separated_Bikeway
                  | Local_Street_Bikeway
                  | Painted_Bike_Lane
                  | Painted_Shared_User_Lane
                  deriving (Show, Eq)
-- interp. the type of bike lane in use in Vancouver

{-
fn_for_bike_route br
    | ((==) Separated_Bikeway br) = (...)
    | ((==) Local_Street_Bikeway br) = (...)
    | ((==) Painted_Bike_Lane br) = (...)
    | ((==) Painted_Shared_User_Lane br) = (...)
-}


-- FUNCTIONS
is_exclusive :: BikeRoute -> Bool
-- Return true if BikeRoute is exclusively used for bicycles

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (is_exclusive Separated_Bikeway) True
            print $check_expect' (is_exclusive Local_Street_Bikeway) False
            print $check_expect' (is_exclusive Painted_Bike_Lane) True
            print $check_expect' (is_exclusive Painted_Shared_User_Lane) False

is_exclusive br -- = False
      | ((==) Separated_Bikeway br) = True
      | ((==) Local_Street_Bikeway br) = False
      | ((==) Painted_Bike_Lane br) = True
      | ((==) Painted_Shared_User_Lane br) = False