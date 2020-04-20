# Copyright (c) 2020 stonatm@gmail.com
# 5x5 characters pixmap font
# fonts based and complete with missing chars from:
# https://www.1001fonts.com/5x5-font.html
# oryginally created by Juan A. Zamarrip (dabnotu)
# site: dabnotu@mastodon
# contact: dabnotu@tuta.io
# fonts contains characters from 32 to 127 in ascii code

def get_letter(asci):

  #capture characters beyound 127
  if asci == 176:
    return celsius
  if asci == 248:
    return celsius
  #capture codes out of range
  if asci < 32:
    return empty
  if asci > 127:
    return empty
  #return valid character in range
  return data[(25*(asci-32)):(25*(asci-32+1))]


empty = [
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0
  ]

celsius = [
  #176
  0,1,1,1,0,
  0,1,0,1,0,
  0,1,1,1,0,
  0,0,0,0,0,
  0,0,0,0,0
  ]

data = [
  #32 SPACE
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  #33 !
  0,0,1,1,0,
  0,0,1,1,0,
  0,0,1,1,0,
  0,0,0,0,0,
  0,0,1,1,0,
  #34 "
  0,1,1,0,1,
  1,1,0,1,1,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  #35 #
  0,1,0,1,0,
  1,1,1,1,1,
  0,1,0,1,0,
  1,1,1,1,1,
  0,1,0,1,0,
  #36 $
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  #37 %
  1,1,0,1,1,
  1,0,1,1,0,
  0,0,1,0,0,
  0,1,1,0,1,
  1,1,0,1,1,
  #38 &
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  #39 '
  0,0,1,1,0,
  0,0,1,1,0,
  0,0,0,1,0,
  0,0,0,0,0,
  0,0,0,0,0,
  #40 (
  0,0,1,1,0,
  0,1,1,0,0,
  0,1,0,0,0,
  0,1,1,0,0,
  0,0,1,1,0,
  #41 )
  0,1,1,0,0,
  0,0,1,1,0,
  0,0,0,1,0,
  0,0,1,1,0,
  0,1,1,0,0,
  #42 *
  1,0,1,0,1,
  0,1,1,1,0,
  1,1,1,1,1,
  0,1,1,1,0,
  1,0,1,0,1,
  #43 +
  0,0,1,0,0,
  0,0,1,0,0,
  1,1,1,1,1,
  0,0,1,0,0,
  0,0,1,0,0,
  #44 ,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,1,1,0,
  0,1,1,0,0,
  #45 -
  0,0,0,0,0,
  0,0,0,0,0,
  0,1,1,1,1,
  0,0,0,0,0,
  0,0,0,0,0,
  #46 .
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,1,1,0,0,
  0,1,1,0,0,
  #47 /
  0,0,0,1,1,
  0,0,1,1,1,
  0,1,1,1,0,
  1,1,1,0,0,
  1,1,0,0,0,
  #48 0
  0,1,1,1,0,
  1,1,0,1,1,
  1,1,0,1,1,
  1,1,0,1,1,
  0,1,1,1,0,
  #49 1
  0,0,1,0,0,
  0,1,1,0,0,
  0,0,1,0,0,
  0,0,1,0,0,
  1,1,1,1,1,
  #50 2
  1,1,1,1,0,
  1,0,0,1,1,
  0,0,1,1,1,
  0,1,1,0,0,
  1,1,1,1,1,
  #51 3
  1,1,1,1,0,
  1,0,0,1,1,
  0,0,1,1,0,
  1,0,0,1,1,
  1,1,1,1,0,
  #52 4
  0,0,1,1,0,
  0,1,1,1,0,
  1,1,0,1,0,
  1,1,1,1,1,
  0,0,0,1,0,
  #53 5
  1,1,1,1,1,
  1,0,0,0,0,
  1,1,1,1,1,
  0,0,0,1,1,
  1,1,1,1,0,
  #54 6
  0,1,1,1,0,
  1,1,0,0,0,
  1,1,1,1,1,
  1,1,0,1,1,
  0,1,1,1,0,
  #55 7
  1,1,1,1,1,
  1,0,0,0,1,
  0,0,0,1,1,
  0,0,1,1,0,
  0,0,1,0,0,
  #56 8
  0,1,1,1,0,
  1,1,0,1,1,
  0,1,1,1,0,
  1,1,0,1,1,
  0,1,1,1,0,
  #57 9
  0,1,1,1,0,
  1,1,0,1,1,
  1,1,1,1,1,
  0,0,0,1,1,
  0,1,1,1,0,
  #58 :
  0,0,0,0,0,
  0,0,1,1,0,
  0,0,0,0,0,
  0,0,1,1,0,
  0,0,0,0,0,
  #59 ;
  0,0,0,0,0,
  0,0,1,1,0,
  0,0,0,0,0,
  0,0,1,1,0,
  0,1,1,0,0,
  #60 <
  0,0,1,0,0,
  0,1,1,0,0,
  1,1,0,0,0,
  0,1,1,0,0,
  0,0,1,0,0,
  #61 =
  0,0,0,0,0,
  0,1,1,1,0,
  0,0,0,0,0,
  0,1,1,1,0,
  0,1,1,1,0,
  #62 >
  0,0,1,0,0,
  0,0,1,1,0,
  0,0,0,1,1,
  0,0,1,1,0,
  0,0,1,0,0,
  #63 ?
  1,1,1,1,0,
  1,0,0,1,1,
  0,0,1,1,0,
  0,0,0,0,0,
  0,0,1,1,0,
  #64 @
  0,1,1,1,0,
  1,0,1,1,1,
  1,0,1,1,1,
  1,1,0,0,0,
  0,1,1,1,0,
  #65 A
  0,1,1,1,0,
  0,1,0,1,0,
  1,1,1,1,1,
  1,0,0,0,1,
  1,1,0,1,1,
  #66 B
  1,1,1,1,0,
  0,1,0,1,1,
  1,1,1,1,0,
  0,1,0,1,1,
  1,1,1,1,0,
  #67 C
  0,0,1,1,1,
  0,1,1,0,1,
  1,1,0,0,0,
  0,1,1,0,1,
  0,0,1,1,1,
  #68 D
  1,1,1,1,0,
  0,1,0,1,1,
  0,1,0,1,1,
  0,1,0,1,1,
  1,1,1,1,0,
  #69 E
  1,1,1,1,1,
  0,1,0,0,1,
  1,1,1,0,0,
  0,1,0,0,1,
  1,1,1,1,1,
  #70 F
  1,1,1,1,1,
  0,1,0,0,1,
  1,1,1,0,0,
  0,1,0,0,0,
  1,1,1,0,0,
  #71 G
  0,1,1,1,0,
  1,1,0,0,0,
  1,0,0,1,1,
  1,1,0,0,1,
  0,1,1,1,1,
  #72 H
  1,1,0,1,1,
  0,1,0,0,1,
  0,1,1,1,1,
  0,1,0,0,1,
  1,1,0,1,1,
  #73 I
  1,1,1,1,1,
  0,0,1,0,0,
  0,0,1,0,0,
  0,0,1,0,0,
  1,1,1,1,1,
  #74 J
  1,1,1,1,1,
  0,0,1,0,0,
  0,0,1,0,0,
  1,0,1,0,0,
  1,1,1,0,0,
  #75 K
  1,0,0,1,1,
  1,0,1,1,0,
  1,1,1,0,0,
  1,0,1,1,0,
  1,0,0,1,1,
  #76 L
  1,1,1,0,0,
  0,1,0,0,0,
  0,1,0,0,0,
  0,1,0,0,1,
  1,1,1,1,1,
  #77 M
  1,1,0,1,1,
  1,1,1,1,1,
  1,0,1,0,1,
  1,0,0,0,1,
  1,1,0,1,1,
  #78 N
  1,1,0,0,1,
  1,1,1,0,1,
  1,0,1,0,1,
  1,0,1,1,1,
  1,0,0,1,1,
  #79 O
  0,1,1,1,0,
  1,1,1,1,1,
  1,0,0,0,1,
  1,1,1,1,1,
  0,1,1,1,0,
  #80 P
  1,1,1,1,0,
  0,1,0,1,1,
  0,1,1,1,0,
  0,1,0,0,0,
  1,1,1,0,0,
  #81 Q
  0,1,1,1,0,
  1,1,0,1,1,
  0,1,1,1,0,
  0,0,1,0,0,
  0,0,1,1,1,
  #82 R
  1,1,1,1,1,
  0,1,1,0,1,
  1,1,1,1,1,
  0,1,0,1,0,
  1,1,0,1,1,
  #83 S
  0,1,1,1,1,
  1,1,0,0,0,
  1,1,1,1,1,
  0,0,0,1,1,
  1,1,1,1,0,
  #84 T
  1,1,1,1,1,
  1,0,1,0,1,
  0,0,1,0,0,
  0,0,1,0,0,
  0,1,1,1,0,
  #85 U
  1,0,0,0,1,
  1,0,0,0,1,
  1,0,0,0,1,
  1,1,0,1,1,
  0,1,1,1,0,
  #86 V
  1,0,0,0,1,
  1,1,0,1,1,
  0,1,0,1,0,
  0,1,1,1,0,
  0,0,1,0,0,
  #87 W
  1,0,0,0,1,
  1,0,1,0,1,
  1,0,1,0,1,
  1,1,1,1,1,
  0,1,0,1,0,
  #88 X
  1,0,0,0,1,
  1,1,0,1,1,
  0,1,1,1,0,
  1,1,0,1,1,
  1,0,0,0,1,
  #89 Y
  1,0,0,0,1,
  1,1,0,1,1,
  0,1,1,1,0,
  0,0,1,0,0,
  0,1,1,1,0,
  #90 Z
  1,1,1,1,1,
  1,0,1,1,0,
  0,0,1,0,0,
  0,1,1,0,1,
  1,1,1,1,1,
  #91 [
  0,1,1,1,0,
  0,1,1,0,0,
  0,1,1,0,0,
  0,1,1,0,0,
  0,1,1,1,0,
  #92 \
  1,1,0,0,0,
  1,1,1,0,0,
  0,1,1,1,0,
  0,0,1,1,1,
  0,0,0,1,1,
  #93 ]
  0,1,1,1,0,
  0,0,1,1,0,
  0,0,1,1,0,
  0,0,1,1,0,
  0,1,1,1,0,
  #94 ^
  0,0,1,0,0,
  0,1,1,1,0,
  1,1,0,1,1,
  0,0,0,0,0,
  0,0,0,0,0,
  #95 _
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  1,1,1,1,1,
  1,1,1,1,1,
  #96 '
  0,1,1,0,0,
  0,0,1,1,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  #97 a
  0,1,1,1,0,
  0,0,0,1,1,
  1,1,1,1,1,
  1,1,0,1,1,
  0,1,1,1,0,
  #98 b
  1,1,0,0,0,
  0,1,0,0,0,
  0,1,1,1,0,
  0,1,0,1,1,
  1,1,1,1,0,
  #99 c
  0,1,1,1,0,
  1,1,0,1,1,
  1,0,0,0,0,
  1,1,0,1,1,
  0,1,1,1,0,
  #100 d
  0,0,0,1,1,
  0,0,0,1,0,
  0,1,1,1,0,
  1,1,0,1,0,
  0,1,1,1,1,
  #101 e
  0,1,1,1,0,
  1,1,0,1,1,
  1,1,1,1,1,
  1,1,0,0,0,
  0,1,1,1,0,
  #102 f
  0,0,1,1,1,
  0,0,1,0,0,
  1,1,1,1,1,
  0,0,1,0,0,
  0,1,1,1,0,
  #103 g
  0,0,1,1,1,
  0,1,1,0,1,
  0,0,1,1,1,
  1,0,0,0,1,
  1,1,1,1,1,
  #104 h
  1,1,0,0,0,
  0,1,0,0,0,
  0,1,1,1,0,
  0,1,0,1,0,
  1,1,0,1,1,
  #105 i
  0,0,1,0,0,
  0,0,0,0,0,
  0,1,1,0,0,
  0,0,1,0,0,
  1,1,1,1,1,
  #106 j
  0,0,0,0,1,
  0,0,0,0,0,
  0,0,0,1,1,
  1,0,0,0,1,
  1,1,1,1,1,
  #107 k
  1,1,0,0,0,
  0,1,0,1,1,
  0,1,1,1,0,
  0,1,0,1,1,
  1,1,0,0,1,
  #108 l
  0,1,1,0,0,
  0,0,1,0,0,
  0,0,1,0,0,
  0,0,1,0,0,
  1,1,1,1,1,
  #10 m
  1,0,0,0,0,
  1,1,1,1,1,
  1,0,1,0,1,
  1,0,1,0,1,
  1,0,1,0,1,
  #110 n
  1,0,0,0,0,
  1,1,1,1,0,
  1,0,0,1,0,
  1,0,0,1,0,
  1,0,0,1,1,
  #111 o
  0,0,1,0,0,
  0,1,1,1,0,
  1,1,0,1,1,
  0,1,1,1,0,
  0,0,1,0,0,
  #112 p
  1,1,1,1,0,
  1,1,0,1,1,
  1,1,1,1,0,
  1,0,0,0,0,
  1,1,0,0,0,
  #113 q
  0,1,1,1,1,
  1,1,0,1,1,
  0,1,1,1,1,
  0,0,0,0,1,
  0,0,0,1,1,
  #114 r
  1,1,0,1,1,
  0,1,1,1,1,
  0,1,0,0,1,
  0,1,0,0,0,
  1,1,1,0,0,
  #115 s
  0,1,0,0,0,
  1,1,0,0,0,
  0,1,1,1,0,
  0,0,0,1,1,
  1,1,1,1,0,
  #116 t
  0,0,1,0,0,
  0,0,1,0,0,
  1,1,1,1,1,
  0,0,1,0,0,
  0,0,1,1,1,
  #117 u
  1,0,0,1,1,
  1,0,0,1,0,
  1,0,0,1,0,
  1,0,0,1,0,
  1,1,1,1,1,
  #118 v
  1,1,0,1,1,
  1,0,0,0,1,
  1,1,0,1,1,
  0,1,1,1,0,
  0,0,1,0,0,
  #119 w
  0,0,1,0,0,
  1,0,1,0,1,
  1,0,1,0,1,
  1,1,1,1,1,
  0,1,0,1,0,
  #120 x
  1,1,0,1,1,
  0,1,1,1,0,
  0,0,1,0,0,
  0,1,1,1,0,
  1,1,0,1,1,
  #121 y
  1,1,0,1,1,
  0,1,0,1,0,
  0,1,1,1,0,
  0,0,1,1,0,
  1,1,1,0,0,
  #122 z
  1,1,1,1,1,
  0,0,0,1,1,
  0,1,1,1,0,
  1,1,0,0,0,
  1,1,1,1,1,
  #123 {
  0,0,1,1,0,
  0,0,1,0,0,
  0,1,1,0,0,
  0,0,1,0,0,
  0,0,1,1,0,
  #124 |
  0,0,1,1,0,
  0,0,1,1,0,
  0,0,1,1,0,
  0,0,1,1,0,
  0,0,1,1,0,
  #125 }
  0,1,1,0,0,
  0,0,1,0,0,
  0,0,1,1,0,
  0,0,1,0,0,
  0,1,1,0,0,
  #126 ~
  0,0,0,0,0,
  1,1,0,0,0,
  0,1,1,1,0,
  0,0,0,1,1,
  0,0,0,0,0,
  #127
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0,
  0,0,0,0,0
  ]


