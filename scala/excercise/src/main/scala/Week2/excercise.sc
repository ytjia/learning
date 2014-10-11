object rationals{
    val t = new Rational(1, 2)
    t.numer
}

class Rational(x: Int, y: Int){
    require(y != 0, "Denominator must be nonzero")
    private def gcd(a: Int, b: Int): Int =
        if (b == 0) a else gcd(b, a % b)
    private def g = gcd(x, y)
    def numer = x / g
    def denom = y / g

    def neg: Rational = new Rational(-numer, denom)
    def add(that: Rational) = {
        new Rational(
            numer * that.denom + that.numer * denom,
            denom * that.denom
        )
    }
    def sub(that: Rational) = add(that.neg)
    def mul(that: Rational) = {
        new Rational(
            numer * that.numer, denom * that.denom)
    }
}
