use std::ops::Index;

pub type DistX = i8;
pub type DistY = i8;
pub type Coord = (DistX, DistY);
pub type Matrix = [Coord; NODE_CT];

pub const NODE_CT: usize = 6;
pub const GRAPH1: Matrix = [(0, 0), (0, 1), (0, -2), (0, 5), (0, -10), (0, 21)];
pub const GRAPH2: Matrix = [(-3, 0), (-3, 1), (0, 0), (0, 1), (3, 0), (3, 1)];

pub type Distance = f32;
pub type NodeIndex = usize;
pub type NeighDist = (NodeIndex, Distance);

// This is different from a regular graph's adjacency list because:
// - iteration is ordered (though starting point doesn't necessarily need to be fixed)
// - each node is connected to two other nodes (or possibly one, if it is an edge node)
pub struct TourAdjList {
    vs: [Option<NeighDist>; NODE_CT],
}

impl Index<usize> for TourAdjList {
    type Output = Option<NeighDist>;

    fn index(&self, index: usize) -> &Self::Output {
        &self.vs[index]
    }
}

impl IntoIterator for TourAdjList {
    type Item = Distance;
    type IntoIter = TourAdjListIter;

    fn into_iter(self) -> Self::IntoIter {
        TourAdjListIter {
            al: self,
            curr: Some(0),
        }
    }
}

pub struct TourAdjListIter {
    al: TourAdjList,
    curr: Option<NodeIndex>,
}

impl Iterator for TourAdjListIter {
    type Item = Distance;

    fn next(self: &mut TourAdjListIter) -> Option<Self::Item> {
        self.curr
            .and_then(|i: NodeIndex| self.al.vs[i])
            .and_then(|(next, dist): NeighDist| {
                self.curr = Some(next);
                Some(dist)
            })
    }
}

fn main() {
    let nnal1: TourAdjList = nearest_neighbor(GRAPH1);
    let nnal2: TourAdjList = nearest_neighbor(GRAPH2);

    let nnal1_dist: f32 = calc_dist(nnal1);
    let nnal2_dist: f32 = calc_dist(nnal2);

    println!(
        "Nearest neighbor heuristic's calculated shortest distance for GRAPH1: {}",
        nnal1_dist
    );

    println!(
        "Nearest neighbor heuristic's calculated shortest distance for GRAPH2: {}",
        nnal2_dist
    );
}

fn calc_dist(al: TourAdjList) -> f32 {
    TourAdjList::into_iter(al).sum()
}

fn get_dist(p1: Coord, p2: Coord) -> f32 {
    f32::sqrt(f32::powi(((p1.0) - (p2.0)) as f32, 2) + f32::powi(((p1.1) - (p2.1)) as f32, 2))
}

fn nearest_neighbor(mat: Matrix) -> TourAdjList {
    // NearestNeighbor(P)
    // Pick and visit an initial point p0 from P
    // p = p0
    // i=0
    // While there are still unvisited points
    //   i=i+1
    //   Select pi to be the closest unvisited point to pi−1
    //   Visit pi
    // Return to p0 from pn−1
    let mut p_n: (NodeIndex, Coord) = (0, mat[0]);
    let mut visited: Vec<NodeIndex> = vec![p_n.0];

    let mut p_n_plus1: (NodeIndex, Distance, Coord);
    let mut result = TourAdjList {
        vs: [None; NODE_CT],
    };

    while visited.len() < NODE_CT {
        p_n_plus1 = {
            let mut min_dist: f32 = f32::INFINITY;
            let mut d: f32;
            let mut c: (NodeIndex, Distance, Coord) = (0, min_dist, (0, 0)); // TODO check if default value is ever used
            for (i, xy) in mat.iter().enumerate() {
                if !visited.contains(&i) {
                    d = get_dist(p_n.1, *xy);
                    if d < min_dist {
                        min_dist = d;
                        c = (i, min_dist, *xy);
                    }
                }
            }
            c
        };
        result.vs[p_n.0] = Some((p_n_plus1.0, p_n_plus1.1));
        visited.push(p_n_plus1.0);
        p_n = (p_n_plus1.0, p_n_plus1.2);
    }

    result
}
