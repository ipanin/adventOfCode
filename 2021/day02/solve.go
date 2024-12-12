package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
)

type Command struct {
	dir string
	n int
}

func ReadCommands(r io.Reader) ([]Command, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)

	var result []Command
	var cmd Command

	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%s %d", &cmd.dir, &cmd.n)
		if err != nil {
			return nil, err
		}

		result = append(result, cmd)
	}

	return result, scanner.Err()
}

func main()  {
	f, err := os.Open("day02/input.txt")
	if err != nil {
		log.Fatal(err)
	}

	input, err := ReadCommands(f)
	f.Close()
	if err != nil {
		log.Fatal(err)
	}

	var x,y,y2 int
	for _, cmd := range input {
		switch cmd.dir {
		case "down":
			y += cmd.n
		case "up":
			y -= cmd.n
		case "forward":
			x += cmd.n
			y2 += y * cmd.n
		}
	}

	fmt.Println("Part1: ", x*y)
	fmt.Println("Part2: ", x*y2)
}


