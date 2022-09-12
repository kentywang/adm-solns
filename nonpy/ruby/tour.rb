GRAPH1 = [[0, 0], [0, 1], [0, -2], [0, 5], [0, -10], [0, 21]]
GRAPH2 = [[-3, 0], [-3, 1], [0, 0], [0, 1], [3, 0], [3, 1]]

def dist(a, b)
  Math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
end

def nearest_neighbor(g)
  visited = [0]
  total_dist = 0
  get_unvisited_indices = -> {
    unv = []
    g.each_with_index { |_, i| unv << i unless visited.include? i }
    unv
  }

  get_closest_i_dist = -> (i_choices, curr_pt_i) {
    curr_i_dist = [-1, Float::INFINITY]
    i_choices.each { |i|
      new_dist = dist(g[curr_pt_i], g[i])
      if new_dist < curr_i_dist[1]
        curr_i_dist = [i, new_dist]
      end
    }
    curr_i_dist
  }

  until visited.length == g.length
    curr = visited.last
    unv = get_unvisited_indices.call
    raise "err" if unv.empty?
    i, dist = get_closest_i_dist.call(unv, curr)
    total_dist += dist
    visited << i
  end

  puts(total_dist)
  puts(visited.join(', '))
end



puts nearest_neighbor(GRAPH1)
puts nearest_neighbor(GRAPH2)

  # - TS
  # - Python
  # - Scala
  # - Scheme
  # - C
  # - Haskell
  # - Rust
  # - Java
  # - Swift
  # - CLisp
  # - Php
  # - C++
  # - Ruby