//g++ solve.cpp -std=c++2a

#include <span>
#include <fstream>
#include <vector>
#include <iostream>

int SonarSweep(std::span<const int> depths, int window_width);

int main() {
    std::ifstream input_file{"input.txt"};
    const std::vector depths(std::istream_iterator<int>{input_file}, {});
    
    int part1 = SonarSweep(depths, 1);
    int part2 = SonarSweep(depths, 3);
    std::cout << "Part1: " << part1 << std::endl;
    std::cout << "Part2: " << part2 << std::endl;
}

int SonarSweep(std::span<const int> depths, int window_width) {
    int increased = 0;
    
    for (int i = window_width; i < depths.size(); ++i) {
        if (depths[i - window_width] < depths[i]) {
            ++increased;
        }
    }

    return increased;
}
