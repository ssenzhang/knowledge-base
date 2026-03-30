#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
#include <map>
#include <string>

// Exercise 1：选择问题
// 有一组N个数，确定其中第k个最大值。k = N / 2。
void exercise_1()
{
    int N = 0;
    std::vector<int> nums;
    std::cin >> N;
    for(int i = 0; i < N; i++)
    {
        int num = 0;
        std::cin >> num;
        nums.push_back(num);
    }
    std::sort(nums.begin(), nums.end());
    std::cout << nums[N / 2];
}

void exercise_1_auto()
{
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> dist(1, 10000000);
    std::vector<int> cases = {100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000};
    std::map<int, double> results;
    std::map<int, double> results_nth;

    for (int i = 0; i < cases.size(); i++)
    {
        int N = cases[i];
        std::vector<int> nums(N);
        for(auto& num : nums)
        {
            num = dist(rng);
        }
        auto bak = nums;

        double total = 0, total_nth = 0;
        int repeats = N <= 1000 ? 10000 : (N <= 10000 ? 1000 : (N <= 100000 ? 100 : 5));
        for(int j = 0; j < repeats; j++)
        {
            auto t0 = std::chrono::high_resolution_clock::now();
            std::sort(nums.begin(), nums.end());
            int result = nums[N / 2];
            auto t1 = std::chrono::high_resolution_clock::now();
            total += std::chrono::duration<double, std::micro> (t1 - t0).count();

            nums = bak;
            t0 = std::chrono::high_resolution_clock::now();
            // std::nth_element(nums.begin(), nums.begin() + N / 2 ,nums.end());  // ascending
            std::nth_element(nums.begin(), nums.begin() + N / 2, nums.end(), std::greater<int>());  // descending
            int result_nth = nums[N / 2];
            t1 = std::chrono::high_resolution_clock::now();
            total_nth += std::chrono::duration<double, std::micro> (t1 - t0).count();

        }
        double elapsed = total / repeats;
        double elapsed_nth = total_nth / repeats;
        results[N] = elapsed;        
        results_nth[N] = elapsed_nth;        
    }

    const int w1 = 10, w2 = 14, w3 = 18;
    std::string sep(w1 + w2 + w3 + 10, '-');
    std::cout << sep << std::endl;
    std::cout << "| " << std::setw(w1) << "N" << " | " << std::setw(w2) << "Elapsed Time" << " | " << std::setw(w3) << "Elapsed Time(nth)" << " |\n";
    std::cout << sep << std::endl;
    auto fmt_time = [](double us)
    {
        if(us < 1000)
        {
            return std::to_string(int(us + 0.5)) + " us";
        }
        else if(us < 1000000)
        {
            char buf[32] = {0};
            std::snprintf(buf, sizeof(buf), "%.2f ms", us / 1000.0);
            return std::string(buf);
        }
        char buf[32] = {0};
        std::snprintf(buf, sizeof(buf), "%.2f s", us / 1000000.0);  
        return std::string(buf);
    };
    for(auto & r : results)
    {
        std::cout << "| " << std::setw(w1) << r.first << " | " << std::setw(w2) << fmt_time(r.second) << " | " << std::setw(w3) << fmt_time(results_nth[r.first]) <<  " |\n";
    }
    std::cout << sep << std::endl;
}

// Exercise 2：解字迷游戏
// 输入由一个由二维字母数组和一个单词表组成，目标是找出字谜中的单词
//   1 2 3 4
// 1 t h i s
// 2 w a t s
// 3 o a h g
// 4 f g d t
// this, two, fat, that
void exercise_2()
{
    const std::vector<std::vector<char>> grid = {
        {'t', 'h', 'i', 's'},
        {'w', 'a', 't', 's'},
        {'o', 'a', 'h', 'g'},
        {'f', 'g', 'd', 't'},
    };
    const std::vector<std::string> words = {"this", "two", "fat", "that", "one"};
    const std::vector<std::vector<int>> dirs = {
        {0, 1}, {0, -1}, {1, 0}, {-1, 0},
        {-1, 1}, {1, -1}, {-1, -1}, {1, 1}
    };
    int rows = grid.size();
    for(int r = 0; r < rows; r++)
    {        
        int cols = grid[r].size();
        for(int c = 0; c < cols; c++)
        {
            for(int i = 0; i < words.size(); i++)
            {
                for(int d = 0; d < dirs.size(); d++)
                {
                    int dr = r, dc = c;
                    bool matched = true;
                    for(int j = 0; j < words[i].size(); j++)
                    {
                        if(dr < 0 || dc < 0 || dr >= rows || dc >= cols || grid[dr][dc] != words[i][j])
                        {
                            matched = false;
                            break;
                        }
                        dr +=dirs[d][0];
                        dc +=dirs[d][1];
                    }
                    if(matched)
                    {
                        std::cout << words[i] << std::endl;
                    }
                }
            }
        }
    }
}

int main()
{
    // exercise_1_auto();
    exercise_2();

    // std::cout << "Press Enter to continue...";
    // std::cin.get();
}