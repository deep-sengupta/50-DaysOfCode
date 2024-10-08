#!/bin/bash

checker() {
    local dns_val=$1
    local ip_values=()
    local avail=false

    if [[ -z "$dns_val" ]]; then
        echo "Error: DNS is required"
        exit 1
    fi

    if ! [[ "$dns_val" =~ ^[a-zA-Z0-9.-]+$ ]]; then
        echo "Error: DNS must be a valid string"
        exit 1
    fi

    ip_values=$(dig +short "$dns_val" A)

    if [[ -z "$ip_values" ]]; then
        avail=true
    fi

    response=$(cat <<EOF
{
    "DNS": "$dns_val",
    "IP": "$(echo "$ip_values" | paste -sd ',')",
    "AVAIL": $avail
}
EOF
)
    echo "$response"
}

echo "Enter the DNS:"
read dns_val

checker "$dns_val"