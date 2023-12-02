package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	var inputPath string
	flag.StringVar(&inputPath, "input", "", "Input file path")
	flag.Parse()
	if inputPath == "" {
		flag.Usage()
		log.Fatalln("Input file path is required.")
	}

	fileContents, err := os.ReadFile(inputPath)
	if err != nil {
		log.Fatalln("Read input file:", err)
	}

	var (
		calibrationValues []int64
		lines             = strings.Split(string(fileContents), "\n")
	)
	for _, line := range lines {
		var numbers []rune
		for _, r := range line {
			if unicode.IsDigit(r) {
				numbers = append(numbers, r)
			}
		}

		numberString := string([]rune{numbers[0], numbers[len(numbers)-1]})

		value, err := strconv.ParseInt(numberString, 10, 64)
		if err != nil {
			log.Printf("parse int %s: %s\n", numberString, err.Error())
			continue
		}

		calibrationValues = append(calibrationValues, value)
	}

	var result int64
	for _, v := range calibrationValues {
		result += v
	}

	fmt.Println(result)
}
