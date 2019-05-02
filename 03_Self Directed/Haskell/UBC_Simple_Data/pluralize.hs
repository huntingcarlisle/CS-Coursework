module Pluralize where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y
    
    main = do   print $check_expect' (pluralize' "Test") "Tests"
                print $check_expect' (pluralize' "") "s"
                print $check_expect' (pluralize' "grass") "grasss"
                print $check_expect' (pluralize' "") "" == False
    
    
    pluralize' :: [Char] -> [Char]
    -- Produce the given string with "s" added to the end.
    
    -- pluralize' n = ""   -- STUB

    pluralize' str = (++) str "s"
    
