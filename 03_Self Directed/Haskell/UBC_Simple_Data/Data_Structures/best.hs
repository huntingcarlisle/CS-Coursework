module Best where

-- DATA DEFINITIONS

data CityName = CityName String deriving (Show)
-- interp. the name of a city

--Examples
cn1 = CityName "Boston"
cn2 = CityName "Vancouver"

{-
fn_for_city_name (CityName cn) =
    (... cn)
-}


-- FUNCTIONS
best_city :: CityName -> Bool
-- Return true if CityName is "Los Angeles"

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (best_city cn1) False
            print $check_expect' (best_city cn2) False
            print $check_expect' (best_city (CityName "Los Angeles")) True

best_city (CityName cn) =
    ((==) cn "Los Angeles")