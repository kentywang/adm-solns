module Main (main) where

main :: IO ()
main = do
  print $ selectionSort []
  print $ selectionSort [1]
  print $ selectionSort [10, 9 .. 1]
  print $ selectionSort [3, 2, 1, 1, 3, 2]
  print $ selectionSortV2 []
  print $ selectionSortV2 [1]
  print $ selectionSortV2 [10, 9 .. 1]
  print $ selectionSortV2 [3, 2, 1, 1, 3, 2]
  print $ selectionSortV3 []
  print $ selectionSortV3 [1]
  print $ selectionSortV3 [10, 9 .. 1]
  print $ selectionSortV3 [3, 2, 1, 1, 3, 2]
  print $ selSort [10, 9 .. 1]
  print $ insSort [10, 9 .. 1]

removeOne :: [Int] -> Int -> [Int]
removeOne [] _ = error "Element not found!"
removeOne list v = case list of
  x : xs | v == x -> xs
  x : xs -> x : removeOne xs v

-- O(n^3) time?
selectionSort :: [Int] -> [Int]
selectionSort [] = []
selectionSort list = do
  mini : selectionSort (removeOne list mini)
  where
    mini = minimum list

-- O(n^2) time?
-- Not even sure if it's still selection sort at this point though
selectionSortV2 :: [Int] -> [Int]
selectionSortV2 [] = []
selectionSortV2 [n] = [n]
selectionSortV2 list = do
  let (m, rest) = minAndRest list
  m : selectionSortV2 rest

minAndRest :: [Int] -> (Int, [Int])
minAndRest [] = error "UNEXPECTED!!!"
minAndRest [n] = (n, [])
minAndRest list = do
  let (m, rest) = minAndRest $ tail list
  case list of
    n : _ | n <= m -> (n, m : rest)
    n : _ -> (m, n : rest)

-- V2, but compacted.
-- looks more like insertion sort than selection, tbh
selectionSortV3 :: [Int] -> [Int]
selectionSortV3 [] = []
selectionSortV3 [x] = [x]
selectionSortV3 (x : xs) = do
  case selectionSortV3 xs of
    [] -> [x]
    y : ys | x <= y -> x : y : ys
    y : ys -> y : selectionSortV3 (x : ys) -- swap happens here, and is what makes this prolly O(n^2)

-- From http://files.farka.eu/pub/AC21007/lec5.pdf
-- My selection sort algos don't come as close as this to describing what we want
selSort :: [Int] -> [Int]
selSort = selSortImpl []
  where
    selSortImpl :: [Int] -> [Int] -> [Int]
    selSortImpl sorted [] = sorted
    selSortImpl sorted xs =
      selSortImpl (sorted ++ [x]) (removeFirst x xs)
      where
        x = minimum xs
        removeFirst _ [] = []
        removeFirst a (x : xs) =
          if x == a
            then xs
            else x : removeFirst a xs

insSort :: [Int] -> [Int]
insSort = insSortImpl []
  where
    insSortImpl :: [Int] -> [Int] -> [Int]
    insSortImpl sorted [] = sorted
    insSortImpl sorted (x : xs) =
      insSortImpl (insert x sorted) xs
      where
        insert y [] = [y]
        insert y (z : zs) =
          if y <= z
            then y : z : zs
            else z : insert y zs
