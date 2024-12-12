package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
)

func ReadInts(r io.Reader) ([]int, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	var result []int
	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return result, err
		}
		result = append(result, x)
	}
	return result, scanner.Err()
}

func main()  {
	f, err := os.Open("day01/input.txt")
	if err != nil {
		log.Fatal(err)
	}

	ints, err := ReadInts(f)
	if err != nil {
		log.Fatal(err)
	}

	part1 := count_increase(ints, 1)
	fmt.Println("Part1: ", part1)

	part2 := count_increase(ints, 3)
	fmt.Println("Part2: ", part2)
}

func count_increase(ints []int, window_size int) int {
	more := 0
	for i := window_size; i < len(ints); i++ {
		// a+b+c < b+c+d if a < d
		if ints[i] > ints[i-window_size] {
			more++
		}
	}
	return more
}

