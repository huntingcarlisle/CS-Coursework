module Yell where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y
    
    main = do   print $check_expect' (yell' "Test") "Test!"
                print $check_expect' (yell' "") "!"
                print $check_expect' (yell' "grass") "grass!"
                print $check_expect' (yell' "") "" == False
    
    
    yell' :: String -> String
    -- produce string with "!" appended
    -- yell' str = ""     STUB

    yell' str = (++) str "!"
    
