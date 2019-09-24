# 서로소 집합들(Disjoint-sets)

## 서로소 집합(Disjoint-sets)

**서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다. 다시 말해 교집합이 없다.**

**집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 대표자(representative)라 한다.**

#### 상호배타 집합을 표현하는 방법

- 연결 리스트
- 트리

#### 상호배타 집합 연산

- Make-Set(x)
- Find-Set(x)
- Union(x, y)



## 상호 배타 집합 표현 - 연결리스트

#### 같은 집합의 원소들은 하나의 연결리스트로 관리한다.

#### 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼는다.

#### 각 원소는 집합의 대표원소를 가리키는 링크를 갖는다.



## 상호 배타 집합 표현 - 트리

#### 하나의 집합(a disjoint set)을 하나의 트리로 표현한다.

#### 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 된다.



## 상호배타 집합에 대한 연산

#### Make-Set( x ) : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

``` c
Make-Set(x)
	p[x] <- x
```



#### Find_set( x ) : x를 포함하는 집합을 갖는 연산

```c
Find-set(x)
    IF x == p[x] : RETURN x
    ELSE : RETURN Find_set(p[x])
```



#### Union( x, y ) : x와 y를 포함하는 두 집합을 통합하는 연산

```c
Union(x, y)
    p[Find-Set(y)] <- Find-Set(x)
```



#### 연산의 효율을 높이는 방법

- Rank를 이용한 Union
  - 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크Rank라는 이름을 저장한다.
  - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.
- Path compression
  - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.



## 같은 트리에 속한 노드인지 확인하는 방법

#### 트리의 대표 원소를 이용

- 간선으로 연결된 노드 중에서 대표 노드를 지정

#### 크루스칼(Kruskal) 알고리즘으로 최소비용신장트리(MST)를 찾을 때 필요한 기술

#### 서로소 집합과 관련

#### 대표값 찾기

```python
rep( n )
	while( p[n] != n )
    	n = p[n]
    return n
```



#### Make_Set() 연산

- Make_Set( x ) : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

```c
p[x] : 노드 x의 부모 저장
rank[x] : 루트 노드가 x인 트리의 랭크 값 저장

Make_Set(x)
    p[x] <- x
    rank[x] <- 0
```



# 최소신장트리(MST)

## 최소신장트리(MST)

#### 그래프에서 최소 비용 문제

1. **<u>모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리</u>**
2. 두 정점 사이의 최소 비용의 경로 찾기



#### 신장 트리

- n개의 정점으로 이루어진 무향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리



#### 최소신장트리(Minimum Spanning Tree)

- 무향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리



#### 그래프

#### 간선들의 배열

#### 인접 리스트

#### 부모 자식관계롸 가중치에 대한 배열

- 트리



## KRUSKAL 알고리즘

#### 간선을 하나씩 선택해서 MST를 찾는 알고리즘

1. 최초, 모든 간선을 가중치에 따라 **오름차순**으로 정렬
2. 가장치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
   1. 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
3. n-1개의 간선이 선택될 때까지 2를 반복



#### 알고리즘

```c
MST-KRUSKAL(G, w)
    A <- 0					// 0: 공집합
    FOR vertex v in G.V		// G.V : 그래프의 정점 집합
    	Make_Set(v)			// G.E : 그래프의 간선 집합
    
    G.E에 포함된 간선들을 가중치 w에 의해 정렬
    
    FOR 가중치가 가장 낮은 간선 (u, v) G.E 선택 (n-1개)
    	IF Find_Set(u) != Find_Set(v)
    		A <- A U {(u, v)}
			union(u, v);
	RETURN A
```



## Prim 알고리즘

#### 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식

1. 임의 정점을 하나 선택해서 시작
2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될 때까지 1, 2 과정을 반복

#### 서로소인 2개의 집합(2 disjoint-sets) 정보를 유지

- 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
- 비트리 정점들(non-tree vertices) - 선택되지 않은 정점들



#### 알고리즘

```c
MST_PRIM(G, r)						// G: 그래프, r: 시작 정점
    FOR u in G.V					
    	u.key <- 무한대			  // u.key : u에 연결된 간선 중 최소 가중치
    	u.pi <- NULL				// u.pi : 트리에서 u의 부모 
    r.key <- 0
    Q <- G.V						// 우선순위 Q에 모든 정점 넣는다.
    WHILE Q != 0					// 빈 Q가 아닐동안 반복
    	u <- Extract_MIN(Q)			// key 값이 가장 작은 정점 가져오기
    	FOR v in G.Adj[u]			// u의 인접 정점들
    		IF v E Q and w(u, v) < v.key	// Q에 있는 v의 key값 갱신
    			v.pi <- u
    			v.key <- w(u, v)
```



# 최단 경로

## 최단 경로

#### 최단 경로 정의

- 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로



#### 하나의 시작 정점에서 끝 정점까지의 최단 경로

- 다익스트라(dijkstra) 알고리즘
  - 음의 가중치를 허용하지 않음
- 벨만-포드(Bellman-Ford) 알고리즘
  - 음의 가중치 허용



#### 모든 정점들에 대한 최단 경로

- 플로이드-워샬(Floyd-Warshall) 알고리즘



## Dijkstra 알고리즘

#### 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식이다.



#### 시작정점(s)에서 끝정점(t)까지의 최단 경로에 정점 x가 존재한다.  이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성된다.



#### 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다.



#### 알고리즘

```c
s: 시작 정점, A: 인접 행렬, D: 거리
V: 정점 집합, U: 선택된 정점 집합

Dijkstra(s, A, D)
    U = {s};

	FOR 모든 정점 v
		D[v] <- A[s][v]
		
    WHILE U != V
    	D[w]가 최소인 정점 w E V-U를 선택
    	U <- U U {w}

		FOR w에 인접한 모든 정점 v
			D[v] <- min(D[v], D[w] + A[w][v])
```



```python
'''
2) 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
을 이렇게 풀어보세요.

물건을 주문하는 지역 좌표(i1, j1)와 각 공장의 위치 좌표(i2, j2)가 주어진다.
물건을 만드는 비용은 지역과 공장의 거리(|i1-i2|+|j1-j2|)로 결정된다면, 
각 물건을 생산하는 최소 비용은 얼마인가? 한 곳의 공장에서 한 개의 물건만 생산한다.
N과 N개의 지역 좌표, N개 공장의 좌표가 차례로 주어진다.
(3 <= N <=7, -100 <= i, j <= 100)
3
-24  -3
-59  5
-2   -79
25   -15
-15  71
-99  -92
'''
```


















