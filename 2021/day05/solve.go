package main

import (
	"bufio"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	vectors, err := ReadAllInts(f)
	if err != nil {
		log.Fatal(err)
	}

	var field map[(int,int)]int

	for vec := range vectors {
		x1,y1,x2,y2 := vec
		drawVector(field, vec)
	}

	res := 0
	for _, val := range field {
		res += (val > 2)
	}

	fmt.Print(res)
}

func ReadAllInts(r io.Reader) ([]int, error) {
	reader := bufio.NewReader(r)
	line, err := reader.ReadString('\n')
	if err != nil {
		return nil, err
	}

	arr := re.
	var res = make([]int, len(arr))

	for i, str := range arr  {
		num, err := strconv.Atoi(str)
		if err != nil {
			return res, err
		}
		res[i] = num
	}
	return res, nil
}
