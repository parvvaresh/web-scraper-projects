package main

import (
	"strings"

	"github.com/PuerkitoBio/goquery"
)

// ExtractPrices parses a tgju.org DOM and extracts price fields based on Persian labels
// mapped to English keys via columnMap.
func ExtractPrices(doc *goquery.Document) map[string]string {
	data := make(map[string]string)
	containers := []string{
		"ul.info-bar.mobile-hide li",
		"ul.info-bar li",
	}
	seen := make(map[string]bool)

	for _, sel := range containers {
		doc.Find(sel).Each(func(i int, s *goquery.Selection) {
			fullText := strings.TrimSpace(s.Text())
			if fullText == "" {
				return
			}
			for fa, en := range columnMap {
				if seen[en] {
					continue
				}
				if strings.Contains(fullText, fa) {
					candidates := []string{
						strings.TrimSpace(s.Find(".value").Text()),
						strings.TrimSpace(s.Find(".info-price").Text()),
						strings.TrimSpace(s.Find("span").Last().Text()),
						fullText,
					}
					for _, c := range candidates {
						if c == "" {
							continue
						}
						if num := firstNumberLike(c); num != "" {
							data[en] = num
							seen[en] = true
							break
						}
					}
				}
			}
		})
	}
	return data
}
