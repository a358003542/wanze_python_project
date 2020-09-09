#!/usr/bin/env python
# -*-coding:utf-8-*-


from copy import deepcopy
from collections import deque

from my_python_module.exceptions import NotAcyclicError
from .directed_graph import DirectedGraph

import logging

logger = logging.getLogger(__name__)


class DirectedAcyclicGraph(DirectedGraph):
    def __init__(self, graph_data=None):
        super().__init__(graph_data=graph_data)

    def add_edge(self, edge):
        """
        加入闭环判断
        """
        super().add_edge(edge)

        if not self.sort():
            raise NotAcyclicError

    def outdegree(self, src):
        """
        Returns the degree of the vertex 'src'
        """
        count = 0
        if src in self.graph_data:
            count = len(self.graph_data[src])

        return count

    def indegree(self, src):
        """
        Returns the in degree of the vertex 'src'
        """
        count = 0
        for k, v in self.graph_data.items():
            if src in v:
                count += 1

        return count

    def remove_edge(self, edge):
        """
        remove edge src -> dest
        """
        src, dest = edge
        super(DirectedAcyclicGraph, self).del_edge((src, dest))

        # clear data
        if self.indegree(src) == 0 and self.outdegree(src) == 0:
            if src in self.graph_data:
                del self.graph_data[src]

        if self.indegree(dest) == 0 and self.outdegree(dest) == 0:
            if dest in self.graph_data:
                del self.graph_data[dest]

    def sort(self):
        """
        L ← Empty list that will contain the sorted elements
        S ← Set of all nodes with no incoming edge
        while S is non-empty do
            remove a node n from S
            add n to tail of L
            for each node m with an edge e from n to m do
                remove edge e from the graph
                if m has no other incoming edges then
                    insert m into S
        if graph has edges then
            return error (graph has at least one cycle)
        else
            return L (a topologically sorted order)
        """
        target = deepcopy(self)
        top_order = []

        queue = deque()
        for k in target.nodes():
            if target.indegree(k) == 0:
                queue.append(k)
                logger.debug('queue append {0}'.format(k))

        while queue:
            n = queue.pop()
            top_order.append(n)

            for m in self.neighbors(n):
                target.remove_edge((n, m))
                logger.debug('remove n->m {0} {1}'.format(n, m))
                if target.indegree(m) == 0:
                    logger.debug('append {0}'.format(m))
                    queue.append(m)

        if len(top_order) != len(self.nodes()):
            return False
        else:
            return top_order
