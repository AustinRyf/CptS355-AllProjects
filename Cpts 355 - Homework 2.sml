(*Austin Ryf - 11512650*)

(*filter, map, and fold*)
fun filter pred [] = [] | 
 	filter pred (x::rest) = 
	if pred x 
	then x::(filter pred rest)
	else (filter pred rest);

fun invFilter pred [] = [] | 
 	invFilter pred (x::rest) = 
	if pred x 
	then (invFilter pred rest)
	else x::(invFilter pred rest);

fun map f [] = [] |
	map f (x::rest) = 
	(f x)::(map f rest);

fun fold f base [] = base | 
 	fold f base (x::rest) = 
	f x (fold f base rest);

fun add x y =
	x + y;


(*numbersToSum function FINISHED*)
fun addup [] = 0 | 
	addup (x::rest) = 
	x + (addup rest);

fun delete [x] = [] |
	delete [] = [] |
	delete (x::rest) =
	if rest = []
	then delete [x]
	else x::(delete rest);

fun numbersToSum sum [] = [] |
	numbersToSum sum (x::rest) =
	if (addup (x::rest)) = sum
	then numbersToSum sum (delete (x::rest))
	else
	if (addup (x::rest)) > sum
	then numbersToSum sum (delete (x::rest))
	else x::rest;


(*numbersToSumTail function FINISHED*)
fun numbersToSumTail sum [] = [] |
	numbersToSumTail sum (x::rest) =
	if sum > x
	then x::(numbersToSumTail (sum - x) rest)
	else numbersToSumTail (sum - x) rest;


(*partition function FINISHED*)
fun partition f [] = ([],[]) |
	partition f L =
	((filter f L)@[], ((invFilter f L)@[]));


(*areAllUnique function & helpers FINISHED*)
fun countInList [] x = 0 |
	countInList (y::rest) x  = 
	if x = y
	then (countInList rest x) + 1
	else (countInList rest x);

fun map f [] = [] |
	map f (x::rest) = 
	(f x)::(map f rest);

fun mapList [] = [] |
	mapList L =
	map (countInList L) L;

fun uniqueChecker [] = true |
	uniqueChecker (x::rest) =
	if x = 1
	then uniqueChecker rest
	else false;

fun areAllUnique [] = true |
	areAllUnique L =
	if uniqueChecker (mapList L) 
	then true
	else false;


(*sum function FINISHED*)
fun map f [] = [] |
	map f (x::rest) = 
	(f x)::(map f rest);

fun fold f base [] = base | 
 	fold f base (x::rest) = 
	f x (fold f base rest);

fun add x y = x + y;

fun addup [] = 0 |
	addup L = 
	fold add 0 L;

fun sum [] = 0 |
	sum [[]] = 0 |
	sum L = 
	addup (map addup L);


(*sumOption function FINISHED*)
fun map f [] = [] |
	map f (x::rest) = 
	(f x)::(map f rest);

fun fold f base [] = base | 
 	fold f base (x::rest) = 
	f x (fold f base rest);

fun addOption (SOME(x)) NONE = SOME(x) |
	addOption NONE (SOME(y)) = SOME(y) |
	addOption NONE NONE = NONE |
	addOption (SOME(x)) (SOME(y)) = SOME(x + y);

fun addupOption [] = NONE |
	addupOption L = 
	fold addOption NONE L;

fun sumOption [] = NONE |
	sumOption [[]] = NONE |
	sumOption L = 
	addupOption (map addupOption L);


(*sumEither function FINISHED*)
datatype either = IString of string | IInt of int;

fun map f [] = [] |
	map f (x::rest) = 
	(f x)::(map f rest);

fun fold f base [] = base | 
 	fold f base (x::rest) = 
	f x (fold f base rest);

fun str2int s = 
	valOf(Int.fromString(s));

fun addEither (IInt(x)) (IString(y)) = IInt(x + str2int y) |
	addEither (IString(x)) (IInt(y)) = IInt(str2int x + y) |
	addEither (IString(x)) (IString(y)) = IInt(str2int x + str2int y) |
	addEither (IInt(x)) (IInt(y)) = IInt(x + y);

fun addupEither [] = (IInt 0) |
	addupEither L = 
	fold addEither (IInt 0) L;

fun sumEither [] = (IInt 0) |
	sumEither [[]] = (IInt 0) |
	sumEither L = 
	addupEither (map addupEither L);


(*depthScan function FINISHED*)
datatype 'a Tree = LEAF of 'a | NODE of 'a * ('a Tree) * ('a Tree);

fun depthScan (NODE(nodeValue, leftNode, rightNode)) = 
	(depthScan(leftNode))@(depthScan(rightNode))@([nodeValue]) | 
	depthScan (LEAF(nodeValue)) = nodeValue::[];


(*depthSearch function FINISHED*)
val myT = NODE(1, NODE (2, NODE(3, LEAF 2 ,LEAF 5),LEAF 1), NODE(1,LEAF 8,LEAF 5));

fun travTree (NODE(nodeValue, leftNode, rightNode)) x =
	if nodeValue = x
	then true
	else
	if (travTree (leftNode) x)
	then travTree (leftNode) x
	else
	if (travTree (rightNode) x)
	then travTree (rightNode) x
	else false |
	travTree (LEAF(nodeValue)) x =
	if nodeValue = x
	then true
	else false;

fun depthHelper (NODE(nodeValue, leftNode, rightNode)) x =
	if nodeValue = x
	then 1
	else
	if (travTree (leftNode) x)
	then 1 + (depthHelper (leftNode) x)
	else if (travTree (rightNode) x)
	then 1 + (depthHelper (rightNode) x)
	else ~1 |
	depthHelper (LEAF(nodeValue)) x =
	if nodeValue = x
	then 1
	else ~1;

fun depthSearch (NODE(nodeValue, leftNode, rightNode)) x =
	if (depthHelper (leftNode) x) > 0
	then 1 + (depthHelper (leftNode) x)
	else 
	if (depthHelper(rightNode) x) > 0
	then 1 + (depthHelper(rightNode) x) 
	else ~1;



(*addTrees function UNFINISHED*)
val T1 = NODE(1, NODE (2, NODE(3, LEAF 4 ,LEAF 5),LEAF 6), NODE(7,LEAF 8,LEAF 9));
val T2 = NODE(1, NODE (2, LEAF 3, LEAF 6), NODE(7, NODE(8, LEAF 10 ,LEAF 11),LEAF 9));

fun addTrees (NODE(nodeValue1, leftNode1, rightNode1)) (NODE(nodeValue2, leftNode2, rightNode2)) =
	if 