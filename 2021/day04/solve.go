package main

// Bingo with squid
// недоделано
import (
	"bufio"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("input_sample.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	draw_numbers, err := ReadCsvInts(f)
	if err != nil {
		log.Fatal(err)
	}

	var boards [][5][5]int
	var number_pos map[int]([][]int)

	for i:=0;; i++ {
		boards[i], err = ReadIntMatrix(f)
		if err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}

		FillNumberPos(number_pos, boards[i])
	}
	for _, number := range draw_numbers {
		pos_arr := number_pos[number]
		for pos := range pos_arr {
			i,j,board_n := pos..;
			boards[board_n][i][j] = -1
			check_win(boards[board_n], i, j)
		}
	}
}

func ReadCsvInts(r io.Reader) ([]int, error) {
	reader := bufio.NewReader(r)
	line, err := reader.ReadString('\n')
	if err != nil {
		return nil, err
	}

	arr := strings.Split(line, ",")
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
