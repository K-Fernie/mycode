#!/bin/bash

function greeting() {

str="Hello, $name"
echo $str
}

echo "Enter your name, now!"
read name

val=$(greeting)
echo "The return value of the function is $val"
