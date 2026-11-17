#!/usr/bin/env bash
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
probe() {
  local u="$1"
  local out
  out=$(curl -sS -o /dev/null -m 20 -A "$UA" -w '%{http_code} %{size_download} %{content_type} %{time_total}' -r 0-0 "$u" 2>/dev/null)
  printf '%-100s %s\n' "$u" "$out"
}
export -f probe
export UA
cat research/urls.txt | xargs -P 8 -I{} bash -c 'probe "{}"'
