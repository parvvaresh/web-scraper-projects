package main

import (
	"strings"
	"testing"

	"github.com/PuerkitoBio/goquery"
)

const sampleHTML = `
<!doctype html><html><body>
<ul class="info-bar mobile-hide">
  <li>دلار <span class="value">۵۸,۹۰۰</span></li>
  <li>انس طلا <span class="info-price">2,345.67</span></li>
  <li>بیت کوین <span>1,234,567</span></li>
</ul>
</body></html>`

func TestExtractPrices(t *testing.T) {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(sampleHTML))
	if err != nil {
		t.Fatalf("goquery.NewDocumentFromReader: %v", err)
	}
	data := ExtractPrices(doc)

	if data["Dollar"] == "" || parseFloatSafe(data["Dollar"]) != 58900 {
		t.Fatalf("Dollar parsed = %q; want ~58900", data["Dollar"])
	}
	if data["GoldOunce"] == "" || parseFloatSafe(data["GoldOunce"]) != 2345.67 {
		t.Fatalf("GoldOunce parsed = %q; want 2345.67", data["GoldOunce"])
	}
	if data["Bitcoin"] == "" || parseFloatSafe(data["Bitcoin"]) != 1234567 {
		t.Fatalf("Bitcoin parsed = %q; want 1234567", data["Bitcoin"])
	}
}
