module SummonStarter where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y

    main = do   print $check_expect' (summon_starter "Test") "accio Test"
                print $check_expect' (summon_starter "Firebolt") "accio Firebolt"

    summon_starter :: [Char] -> [Char]
    -- produces summoning charm based on string input

--    summon_starter n = ""   -- STUB
    summon_starter = ("accio " ++)
