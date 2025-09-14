package main

import (
	"testing"
	"time"
)

func TestNormalizeNumberString(t *testing.T) {
	in := "۱۲۳٬۴۵۶٫۷۸"
	out := normalizeNumberString(in)
	want := "123456.78"
	if out != want {
		t.Fatalf("normalizeNumberString(%q) = %q; want %q", in, out, want)
	}

	in2 := "98٬765,432.10"
	out2 := normalizeNumberString(in2)
	want2 := "98765432.10" // both separators are removed
	if out2 != want2 {
		t.Fatalf("normalizeNumberString(%q) = %q; want %q", in2, out2, want2)
	}
}

func TestParseFloatSafeAndFirstNumberLike(t *testing.T) {
	s := "قیمت دلار: ۵۸,۹۰۰ تومان"
	num := firstNumberLike(s)
	if num == "" {
		t.Fatalf("firstNumberLike failed to find number in: %q", s)
	}
	f := parseFloatSafe(num)
	if f != 58900 {
		t.Fatalf("parseFloatSafe(%q) = %v; want 58900", num, f)
	}
}

func TestGregorianToJalali_NowruzAnchors(t *testing.T) {
	type tc struct {
		gY, gM, gD int
		jY, jM, jD int
	}
	cases := []tc{
		{2024, 3, 20, 1403, 1, 1},
		{2023, 3, 21, 1402, 1, 1},
		{2020, 3, 20, 1399, 1, 1},
		{2017, 3, 21, 1396, 1, 1},
	}
	for _, c := range cases {
		jy, jm, jd := gregorianToJalali(c.gY, c.gM, c.gD)
		if jy != c.jY || jm != c.jM || jd != c.jD {
			t.Fatalf("G2J(%04d-%02d-%02d) = %04d-%02d-%02d; want %04d-%02d-%02d",
				c.gY, c.gM, c.gD, jy, jm, jd, c.jY, c.jM, c.jD)
		}
	}
	// Also sanity check jalaliDateString formatting
	ts := time.Date(2024, 3, 20, 10, 0, 0, 0, time.UTC)
	if got := jalaliDateString(ts); got != "1403-01-01" {
		t.Fatalf("jalaliDateString(2024-03-20) = %s; want 1403-01-01", got)
	}
}
