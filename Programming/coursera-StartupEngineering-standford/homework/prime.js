#!/usr/bin/env node

// is_divisible_by - Is not divisible by any number in array except 1 and itself
var is_not_divisible_by = function(n, arr) 
{
	if (n < 1 || n == 1) { return true;}
	else if (n > 1)
	{ 
		var is_not_divisible = true;
		var i = 0;
		while (is_not_divisible && i < arr.length)
		{
			if (arr[i] != 1 && arr[i] != n) 
			{
				is_not_divisible = ((n % arr[i]) != 0);
			}
			i++;
		}
		return is_not_divisible;
	}
};

// Find prime numbers under K
var PrimeUnderK = function(k) 
{
	var i = 1;
	var arr = [];
	for(i = 1; i < k; i++) 
	{
		if (is_not_divisible_by(i, arr)) { arr.push(i); }
	}
	return arr;
};

// Print to console
var fmt = function(arr) 
{
	return arr.join(", ");
};

var k = 100;
console.log("PrimeUnderK( " + k + " )");
console.log(fmt(PrimeUnderK(k)));
