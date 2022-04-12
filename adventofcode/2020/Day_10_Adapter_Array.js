let input = `77
58
25
92
14
154
105
112
147
63
84
109
24
129
49
102
130
128
134
88
95
70
80
4
153
17
145
122
39
117
93
65
3
2
139
101
148
37
27
1
87
64
23
59
42
146
43
151
116
46
115
118
131
94
19
33
12
107
10
7
73
78
53
11
135
79
60
32
141
31
140
98
136
72
38
152
30
74
106
50
13
26
155
67
20
66
91
56
34
125
52
51
18
108
57
81
119
71
144`
  .split("\n")
  .map((el) => parseInt(el));



let devices_built_in_adapter_voltage = Math.max(...input) + 3;
input.push(0)
input.push(devices_built_in_adapter_voltage)


input.sort((a, b) => a - b);
console.log(input);
// input.sort();

let counter = {
  1: 0,
  2: 0,
  3: 0,
};
for (let i = 1; i < input.length; i++) {
  console.log(input[i], input[i - 1], input[i] - input[i - 1]);
  switch (input[i] - input[i - 1]) {
    case 1:
      counter[1] += 1;
      break;
    case 2:
      counter[2] += 1;
      break;
    case 3:
      counter[3] += 1;
      break;
    default:
      console.log(
        "default case",
        input[i],
        input[i - 1],
        input[i] - input[i - 1]
      );
      break;
  }
}

console.log(counter);
