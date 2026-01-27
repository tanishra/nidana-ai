from backend.utils.logger import get_logger

logger = get_logger(__name__)


def compute_confidence(result):
    """
    Compute doctor-grade confidence for a single disease result
    based on weighted symptom coverage and safety gates.
    """
    matched_common = len(result.get("matched_common", []))
    matched_key = len(result.get("matched_key", []))
    matched_risk = len(result.get("matched_risk", []))

    total_common = max(result.get("total_common", 1), 1)
    total_key = max(result.get("total_key", 1), 1)

    # Coverage ratios
    common_coverage = matched_common / total_common
    key_coverage = matched_key / total_key

    # Weighted confidence (doctor-aligned)
    confidence = (
        common_coverage * 30 +
        key_coverage * 60 +
        min(matched_risk, 1) * 10
    )

    logger.debug(
        "Computed raw confidence | disease=%s, matched_common=%d, matched_key=%d, "
        "matched_risk=%d, confidence=%.2f",
        result.get("disease"),
        matched_common,
        matched_key,
        matched_risk,
        confidence
    )

    # -------------------------
    # SAFETY GATES
    # -------------------------
    total_symptoms = matched_common + matched_key

    # Rule 1: Minimum evidence (at least 2 symptoms)
    if total_symptoms < 2:
        logger.debug(
            "Minimum evidence gate triggered | disease=%s, confidence capped at 30",
            result.get("disease")
        )
        confidence = min(confidence, 30)

    # Rule 2: No key symptom → cap confidence at 50%
    if matched_key == 0:
        logger.debug(
            "No key symptom gate triggered | disease=%s, confidence capped at 50",
            result.get("disease")
        )
        confidence = min(confidence, 50)

    return round(confidence, 2)


def normalize_confidence(results):
    """
    Normalize confidence for a list of disease results using
    weighted evidence coverage and doctor-grade safety rules.
    """
    logger.debug("Starting confidence normalization for results: %s", results)

    if not results:
        logger.debug("No results provided, returning as-is")
        return results

    for r in results:
        r["confidence"] = compute_confidence(r)
        logger.debug(
            "Assigned confidence %.2f to disease=%s",
            r["confidence"],
            r.get("disease")
        )

    sorted_results = sorted(results, key=lambda x: x["confidence"], reverse=True)
    logger.info(
        "Confidence normalization completed | diseases sorted by confidence: %s",
        [r["disease"] for r in sorted_results]
    )

    return sorted_results