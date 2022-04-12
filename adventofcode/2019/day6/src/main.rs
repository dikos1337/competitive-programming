use std::collections::{HashMap, HashSet};

struct Graph<'a> {
    graph: HashMap<&'a str, HashSet<&'a str>>,
    directed: bool,
}

impl<'a> Graph<'a> {
    fn new() -> Self {
        Graph {
            graph: HashMap::new(),
            directed: false,
        }
    }

    #[allow(dead_code)]
    fn new_directed() -> Self {
        Graph {
            graph: HashMap::new(),
            directed: true,
        }
    }

    fn add_edge(&mut self, node1: &'a str, node2: &'a str) {
        self.graph
            .entry(node1)
            .or_insert_with(HashSet::new)
            .insert(node2);

        if !self.directed {
            self.graph
                .entry(node2)
                .or_insert_with(HashSet::new)
                .insert(node1);
        }
    }

    fn add_connections(&mut self, connections: Vec<(&'a str, &'a str)>) {
        for (node1, node2) in connections {
            self.add_edge(node1, node2);
        }
    }

    fn find_path(
        &self,
        node1: &'a str,
        node2: &'a str,
        path: Option<Vec<&'a str>>,
    ) -> Option<Vec<&'a str>> {
        let mut path = path.unwrap_or_default();
        path.push(node1);

        if node1 == node2 {
            return Some(path);
        }
        if !self.graph.contains_key(node1) {
            return None;
        }

        for node in self.graph[node1].iter() {
            if !path.contains(node) {
                if let Some(p) = self.find_path(node, node2, Some(path.clone())) {
                    return Some(p);
                }
            }
        }

        None
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let orbits = input
        .lines()
        .map(|s| s.split(')'))
        .map(|mut s| {
            let a = s.next().unwrap();
            let b = s.next().unwrap();
            (a, b)
        })
        .collect::<Vec<_>>();

    let mut graph = Graph::new();
    graph.add_connections(orbits);

    let mut total_orbits = 0;
    for node in graph.graph.keys() {
        if let Some(path) = graph.find_path("COM", node, None) {
            total_orbits += path.len() - 1;
        }
    }
    println!("Part 1: {}", total_orbits);

    if let Some(part2) = graph.find_path("YOU", "SAN", None) {
        {
            println!("Part 2: {}", part2.len() - 3);
        };
    }
}
