def real(nameWords: Array[String], checksum: String): Boolean = {
    val name = nameWords.mkString
    val charset = name.foldLeft(Set.empty[Char])(_ + _).toList
    val freqs = name.foldLeft(Map.empty[Char, Int].withDefault(_ => 0)) { (map,char) => 
        map.updated(char, map(char) + 1)
    }
    val check = charset.sortWith { (c1,c2) =>
        if(freqs(c1) == freqs(c2)) {
            c1 < c2
        } else {
            freqs(c1) >= freqs(c2)
        }
    }.take(5).mkString
    check == checksum
}

def digit(str: String): Boolean = {
    str.forall(c => '0' <= c && c <= '9')
}

def parse(str: String): (Array[String], Int, String) = {
    val tokens = str.split("(\\-|\\[|\\])")
    val (name, rest) = tokens.span(token => !digit(token))
    val code = rest(0).toInt
    val checksum = rest(1)
    (name,code,checksum)
}

def sumValidSectorIds(lines: Iterable[String]): Int = {
    lines.view
    .map(parse)
    .filter{ case (name,_,checksum) => real(name,checksum) }
    .map{ case (_,code,_) => code }
    .sum
}

/*
assert(real("aaaaabbbzyx", "abxyz"))
assert(real("abcdefgh", "abcde"))
assert(real("notarealroom", "oarel"))
assert(!real("totallyrealroom","decoy"))
*/

val example = List(
    "aaaaa-bbb-z-y-x-123[abxyz]", 
    "a-b-c-d-e-f-g-h-987[abcde]", 
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]"
)
assert(sumValidSectorIds(example) == 1514)

import scala.io.Source

val lines = Source.fromFile("input4.txt").getLines().toIterable
//sumValidSectorIds(lines)

def decode(words: Array[String], code: Int): String = {
    def shift(c: Char): Char = {
        ('a' + (((c - 'a').toInt + (code % 26)) % 26)).toChar
    }
    words.map(_.map(shift)).mkString(" ")
}

def part2() = {
    lines.map(parse)
         .map{ case (words,code,_) => (code,decode(words, code))}
         .filter{ case (_,decoded) => decoded == "northpole object storage" }
         .foreach(println)
}
part2()